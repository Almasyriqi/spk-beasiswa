# 🛠️ Tools

Perkakas pendukung pengembangan. Bukan bagian dari aplikasi — tidak perlu dipasang untuk menjalankan sistem.

---

## `capture_manual.py`

Mengambil seluruh screenshot untuk [`docs/MANUAL.md`](../docs/MANUAL.md) secara otomatis dengan menjalankan aplikasi di peramban sungguhan memakai Playwright.

Tujuannya agar manual tidak cepat basi: ketika tampilan aplikasi berubah, seluruh gambar dapat diperbarui lewat satu perintah, bukan dipotret ulang satu per satu.

### Kebutuhan

```bash
pip install playwright
playwright install chromium
```

### Cara pakai

**1. Jalankan aplikasi atas salinan proyek.**

> ⚠️ **Jangan menjalankannya langsung di direktori repositori.** Menekan tombol `Analisis MOORA` akan **mengosongkan tabel `hasil`** dan menambah akun siswa pada `beasiswa.db`, sehingga berkas basis data yang ikut ter-commit akan berubah.

```bash
cp -r . /tmp/spk-demo && cd /tmp/spk-demo
streamlit run main.py --server.port 8501 --server.headless true
```

**2. Jalankan pengambil screenshot dari direktori repositori.**

```bash
python tools/capture_manual.py --out docs/img
```

### Opsi

| Opsi | Bawaan | Keterangan |
|---|---|---|
| `--url` | `http://localhost:8501/` | Alamat aplikasi yang sedang berjalan |
| `--out` | `docs/img` | Direktori penyimpanan berkas PNG |
| `--template` | `template.csv` | Berkas CSV yang diunggah saat peragaan |
| `--browser` | *(kosong)* | Path executable peramban, bila tidak memakai unduhan bawaan Playwright |

### Yang dihasilkan

21 berkas PNG berukuran 1280 × 800 dengan awalan nomor urut (`01-login.png`, `02-login-terisi.png`, dan seterusnya), meliputi alur pihak sekolah dari login sampai logout, serta alur siswa.

### Catatan implementasi

Beberapa hal yang membuat skrip ini tidak sesederhana "buka halaman lalu potret":

| Hal | Penanganan |
|---|---|
| **Login perlu dua kali tekan** | Perilaku aplikasi, bukan kegagalan skrip — lihat [KI-10](../docs/SRS.md#51-daftar-temuan). Fungsi `login()` menekan tombol dua kali |
| **Menu samping berada di dalam `iframe`** | `streamlit-option-menu` adalah komponen kustom, sehingga kliknya lewat `frame_locator`, bukan `page.click` biasa |
| **Isi tabel tidak ada di `innerText`** | Streamlit menggambar tabel ke `<canvas>`, jadi yang ditunggu adalah keberadaan elemen `.stDataFrame`, bukan teks selnya |
| **Halaman belum selesai dirender** | Menunggu teks atau elemen yang spesifik, bukan jeda waktu tetap, agar tidak ada screenshot berisi spinner |
| **Judul tertutup header** | `gulir_ke()` menyisakan ruang di atas elemen setelah `scrollIntoView` |
| **Galat ikut terpotret** | Screenshot ditolak bila halaman memuat `Traceback` atau `Exception` |
