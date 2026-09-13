"""Pengambil screenshot otomatis untuk docs/MANUAL.md.

Menjalankan aplikasi lewat peramban sungguhan memakai Playwright, menelusuri
alur pihak sekolah dan siswa, lalu menyimpan setiap layar sebagai PNG.

Cara pakai:
    1. Jalankan aplikasi lebih dulu (sebaiknya atas SALINAN proyek, karena
       analisis MOORA mengosongkan tabel `hasil` dan menambah akun siswa):

           streamlit run main.py --server.port 8501 --server.headless true

    2. Jalankan skrip ini:

           python tools/capture_manual.py --out docs/img

Opsi lain: --url (alamat aplikasi), --template (berkas CSV yang diunggah),
--browser (executable peramban, bila tidak memakai unduhan bawaan Playwright).
"""

import argparse
import pathlib
import sys

from playwright.sync_api import sync_playwright

LEBAR, TINGGI = 1280, 800

# Kredensial contoh yang sudah ada pada beasiswa.db bawaan repositori.
AKUN_SEKOLAH = ("smkn1@gmail.com", "12345678")
AKUN_SISWA = ("DimasPermana@gmail.com", "1234")

# Penanda galat; bila muncul di halaman, screenshot ditolak.
PENANDA_GALAT = ("Traceback", "Exception", "StreamlitAPIException")


class Pembidik:
    """Menyimpan screenshot secara berurutan sambil memeriksa kewarasannya."""

    def __init__(self, page, out_dir):
        self.page = page
        self.out = pathlib.Path(out_dir)
        self.out.mkdir(parents=True, exist_ok=True)
        self.n = 0
        self.tersimpan = []

    def _periksa_galat(self, nama):
        teks = self.page.inner_text("body")
        for penanda in PENANDA_GALAT:
            if penanda in teks:
                raise RuntimeError(
                    f"halaman memuat '{penanda}' saat membidik {nama!r} — "
                    "screenshot dibatalkan agar galat tidak ikut terdokumentasi"
                )

    def bidik(self, nama, elemen=None):
        self.n += 1
        berkas = self.out / f"{self.n:02d}-{nama}.png"
        self._periksa_galat(nama)
        if elemen is None:
            self.page.screenshot(path=str(berkas))
        else:
            self.page.locator(elemen).screenshot(path=str(berkas))
        ukuran = berkas.stat().st_size
        if ukuran < 5_000:
            raise RuntimeError(f"{berkas.name} hanya {ukuran} byte — kemungkinan halaman kosong")
        print(f"  {berkas.name:<34} {ukuran // 1024:>4} KB")
        self.tersimpan.append(berkas)
        return berkas


def tunggu_teks(page, teks, timeout=30_000):
    """Menunggu teks benar-benar muncul, bukan sekadar menunggu waktu tertentu."""
    page.wait_for_function(
        "t => document.body.innerText.includes(t)", arg=teks, timeout=timeout
    )
    tunggu_idle(page)


def tunggu_idle(page):
    """Menunggu indikator 'Running' Streamlit selesai."""
    try:
        page.wait_for_function(
            """() => {
                const w = document.querySelector('[data-testid="stStatusWidget"]');
                return !w || w.innerText.trim() === '';
            }""",
            timeout=30_000,
        )
    except Exception:
        pass
    page.wait_for_timeout(600)  # jeda kecil agar animasi tabel selesai


def tunggu_tabel(page, jumlah=1, timeout=30_000):
    """Menunggu tabel selesai dirender.

    Streamlit menggambar tabel ke dalam <canvas>, sehingga isi selnya tidak
    pernah muncul pada innerText. Karena itu yang ditunggu adalah keberadaan
    elemen tabelnya, bukan teks di dalamnya.
    """
    page.wait_for_function(
        "n => document.querySelectorAll('.stDataFrame').length >= n",
        arg=jumlah,
        timeout=timeout,
    )
    tunggu_idle(page)


def gulir_ke(page, teks, jarak_atas=100):
    """Menggulir sampai teks terlihat, dengan sisa ruang di atasnya.

    `scrollIntoView` menempelkan elemen tepat di tepi atas viewport sehingga
    judul tertutup header Streamlit yang melayang. `jarak_atas` menggeser
    guliran ke belakang supaya judulnya utuh terlihat.
    """
    page.evaluate(
        """([t, jarak]) => {
            const el = [...document.querySelectorAll('h1,h2,h3,h4,p,div')]
                .find(e => e.innerText && e.innerText.trim().startsWith(t));
            if (el) {
                el.scrollIntoView({block: 'start'});
                const sc = document.querySelector('section.main') || window;
                if (sc === window) window.scrollBy(0, -jarak);
                else sc.scrollTop -= jarak;
            }
        }""",
        [teks, jarak_atas],
    )
    page.wait_for_timeout(500)


def login(page, url, email, sandi, pembidik=None, prefix="", bidik_kosong=True):
    """Login ke aplikasi.

    Catatan perilaku aplikasi: tombol Login perlu ditekan DUA KALI. Penekanan
    pertama membentuk sesi dan menampilkan pesan 'Logged In As', tetapi menu
    samping baru muncul pada rerun berikutnya (lihat main.py, blok headerSection).
    """
    page.goto(url, wait_until="networkidle")
    tunggu_teks(page, "Login Section")
    if pembidik and bidik_kosong:
        pembidik.bidik(f"{prefix}login")

    page.fill("input[type=text]", email)
    page.fill("input[type=password]", sandi)
    page.wait_for_timeout(400)
    if pembidik:
        pembidik.bidik(f"{prefix}login-terisi")

    page.click("button:has-text('Login')")
    tunggu_teks(page, "Logged In As")
    if pembidik:
        pembidik.bidik(f"{prefix}login-pesan")

    page.click("button:has-text('Login')")  # penekanan kedua memunculkan menu
    tunggu_teks(page, "Halaman Home")


def klik_menu(page, nama):
    """Menu samping adalah komponen kustom di dalam iframe, bukan DOM biasa."""
    frame = page.frame_locator("iframe[title='streamlit_option_menu.option_menu']")
    frame.locator(f".nav-link:has-text('{nama}')").first.click()
    tunggu_idle(page)


def alur_sekolah(page, pembidik, url, template):
    print("\n[1/2] Alur pihak sekolah")
    login(page, url, *AKUN_SEKOLAH, pembidik=pembidik)

    # Halaman Home memuat enam tabel referensi; dibidik per bagian.
    gulir_ke(page, "Halaman Home")
    pembidik.bidik("home-sambutan")
    gulir_ke(page, "Tabel 2")
    pembidik.bidik("home-tabel-2-4")
    gulir_ke(page, "Tabel 5")
    pembidik.bidik("home-tabel-5-6")
    gulir_ke(page, "Cara Penggunaan Sistem")
    pembidik.bidik("home-cara-pakai")
    pembidik.bidik("sidebar-sekolah", elemen='[data-testid="stSidebar"]')

    klik_menu(page, "Input")
    tunggu_teks(page, "Input Data CSV")
    pembidik.bidik("input-kosong")

    page.set_input_files("input[type=file]", template)
    tunggu_teks(page, "template.csv")
    tunggu_tabel(page)
    pembidik.bidik("input-pratayang")

    page.click("button:has-text('Analisis MOORA')")
    tunggu_teks(page, "Hasil Perangkingan Metode MOORA")
    tunggu_tabel(page, jumlah=4)  # pratayang + normalisasi + optimasi + perangkingan
    gulir_ke(page, "Normalisasi Data")
    pembidik.bidik("hasil-normalisasi")
    gulir_ke(page, "Nilai Optimasi")
    pembidik.bidik("hasil-optimasi")
    gulir_ke(page, "Hasil Perangkingan")
    pembidik.bidik("hasil-perangkingan")

    klik_menu(page, "Pengumuman")
    tunggu_teks(page, "Pengumuman Hasil Seleksi Beasiswa")
    pembidik.bidik("pengumuman-sekolah")

    klik_menu(page, "Edit Password")
    tunggu_teks(page, "Edit Password")
    pembidik.bidik("edit-password")

    page.click("button:has-text('Log Out')")
    tunggu_teks(page, "Login Section")
    pembidik.bidik("logout")


def alur_siswa(browser, pembidik_out, url, mulai_dari):
    print("\n[2/2] Alur siswa")
    konteks = browser.new_context(viewport={"width": LEBAR, "height": TINGGI})
    page = konteks.new_page()
    pembidik = Pembidik(page, pembidik_out)
    pembidik.n = mulai_dari

    # Halaman login kosong tidak dibidik ulang: tampilannya identik dengan
    # screenshot pertama, jadi manual cukup merujuk gambar yang sama.
    login(page, url, *AKUN_SISWA, pembidik=pembidik, prefix="siswa-",
          bidik_kosong=False)
    gulir_ke(page, "Halaman Home")
    pembidik.bidik("home-siswa")
    pembidik.bidik("sidebar-siswa", elemen='[data-testid="stSidebar"]')

    klik_menu(page, "Pengumuman")
    tunggu_teks(page, "Pengumuman Hasil Seleksi Beasiswa")
    pembidik.bidik("pengumuman-siswa")

    konteks.close()
    return pembidik.tersimpan


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--url", default="http://localhost:8501/")
    ap.add_argument("--out", default="docs/img")
    ap.add_argument("--template", default="template.csv")
    ap.add_argument("--browser", default=None,
                    help="path executable peramban; kosongkan untuk memakai bawaan Playwright")
    a = ap.parse_args()

    template = str(pathlib.Path(a.template).resolve())
    if not pathlib.Path(template).is_file():
        sys.exit(f"berkas template tidak ditemukan: {template}")

    opsi = {"args": ["--no-sandbox", "--disable-dev-shm-usage"]}
    if a.browser:
        opsi["executable_path"] = a.browser

    print(f"Mengambil screenshot dari {a.url} ke {a.out}/")
    with sync_playwright() as p:
        browser = p.chromium.launch(**opsi)
        konteks = browser.new_context(viewport={"width": LEBAR, "height": TINGGI})
        page = konteks.new_page()
        pembidik = Pembidik(page, a.out)

        alur_sekolah(page, pembidik, a.url, template)
        terakhir = pembidik.n
        konteks.close()

        siswa = alur_siswa(browser, a.out, a.url, terakhir)
        browser.close()

    total = len(pembidik.tersimpan) + len(siswa)
    print(f"\nSelesai — {total} screenshot tersimpan di {a.out}/")


if __name__ == "__main__":
    main()
