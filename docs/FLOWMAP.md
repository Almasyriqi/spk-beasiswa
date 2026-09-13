<div align="center">

# 🗺️ Flowmap & Flowchart

### SPK Beasiswa — Metode MOORA
**SMK Negeri 1 Ciomas, Kabupaten Bogor**

<br/>

![Diagram](https://img.shields.io/badge/diagram-Mermaid-FF3670?style=flat-square&logo=mermaid&logoColor=white)
![Jenis](https://img.shields.io/badge/jenis-flowmap%20%2B%20flowchart-blue?style=flat-square)

</div>

---

## 📑 Daftar Isi

| Bagian | Isi |
|---|---|
| **A** | [Keterangan Simbol](#a-keterangan-simbol) |
| **B** | [Flowmap Dokumen (Swimlane)](#b-flowmap-dokumen-swimlane) |
| **C** | [Narasi Alur per Langkah](#c-narasi-alur-per-langkah) |
| **D** | [Flowchart 1 — Autentikasi & Routing](#d-flowchart-1--autentikasi--routing-berbasis-peran) |
| **E** | [Flowchart 2 — Unggah & Analisis](#e-flowchart-2--unggah--analisis-data) |
| **F** | [Flowchart 3 — Algoritma MOORA](#f-flowchart-3--algoritma-moora) |
| **G** | [Flowchart 4 — Publikasi Pengumuman](#g-flowchart-4--publikasi-pengumuman) |
| **H** | [Diagram Sekuens Sistem](#h-diagram-sekuens-sistem) |

> 📎 **Dokumen terkait:** [SRS](SRS.md) · [Daftar Fitur](FITUR.md) · [README Proyek](../README.md)

---

# A. Keterangan Simbol

Diagram pada dokumen ini digambar dengan **Mermaid** agar ter-render langsung di GitHub. Bentuk node mengikuti konvensi flowmap dan flowchart berikut:

| Bentuk | Notasi Mermaid | Makna |
|---|---|---|
| ⬭ Kapsul | `([...])` | Terminator — awal atau akhir alur |
| ▭ Persegi | `[...]` | Proses atau aktivitas |
| ▱ Jajar genjang | `[/.../]` | Dokumen, masukan, atau keluaran |
| ◇ Belah ketupat | `{...}` | Keputusan atau percabangan |
| ⛁ Silinder | `[(...)]` | Penyimpanan data / basis data |
| ⬚ Aktivitas manual | `[[...]]` | Aktivitas manual di luar sistem |
| → Panah utuh | `-->` | Aliran kendali atau data |
| ⇢ Panah putus | `-.->` | Aliran tidak langsung atau bersifat turunan |

---

# B. Flowmap Dokumen (Swimlane)

Flowmap berikut memperlihatkan perjalanan dokumen dan data antar entitas, dari data mentah siswa sampai pengumuman diterima siswa. Setiap kolom (*swimlane*) mewakili satu entitas yang terlibat.

```mermaid
flowchart TB
    subgraph SEKOLAH["🏫 PIHAK SEKOLAH"]
        direction TB
        A1([Mulai])
        A2[/"Data mentah siswa<br/>SKTM · SADK · PO · JTO · NRRST"/]
        A3[["Login sebagai<br/>pihak sekolah"]]
        A4[/"Template input.csv"/]
        A5[["Konversi data ke<br/>rating kecocokan 1–5"]]
        A6[/"Berkas CSV<br/>matriks keputusan"/]
        A7[["Unggah berkas CSV<br/>di halaman Input"]]
        A8[["Tekan tombol<br/>Analisis MOORA"]]
        A9[/"Berkas hasil<br/>output.csv"/]
        A10([Selesai])
    end

    subgraph SISTEM["⚙️ SISTEM"]
        direction TB
        B1["Verifikasi kredensial<br/>& bentuk sesi"]
        B2["Sediakan template.csv<br/>di halaman Home"]
        B3["Baca berkas CSV &<br/>tampilkan pratayang"]
        B4["Hitung normalisasi<br/>r = x / √Σx²"]
        B5["Hitung nilai optimasi<br/>v = w × r"]
        B6["Hitung Yi<br/>Σbenefit − Σcost"]
        B7["Urutkan Yi menurun &<br/>beri nomor peringkat"]
        B8[/"Tabel normalisasi, optimasi,<br/>dan perangkingan"/]
        B9["Bentuk surel &<br/>simpan akun siswa"]
        B10["Ambil 5 peringkat teratas"]
        B11[/"Halaman Pengumuman"/]
    end

    subgraph DB["🗄️ BASIS DATA"]
        direction TB
        C1[("users")]
        C2[("hasil")]
    end

    subgraph SISWA["🎒 SISWA"]
        direction TB
        D1[["Login dengan<br/>akun otomatis"]]
        D2[["Buka menu Pengumuman"]]
        D3[/"Daftar penerima beasiswa"/]
        D4([Selesai])
    end

    A1 --> A2
    A2 --> A3
    A3 --> B1
    B1 --> B2
    B2 --> A4
    A4 --> A5
    A2 -.->|"Bahan konversi"| A5
    A5 --> A6
    A6 --> A7
    A7 --> B3
    B3 --> A8
    A8 --> B4
    B4 --> B5
    B5 --> B6
    B6 --> B7
    B7 --> B8
    B7 --> B9
    B8 --> A9
    A9 --> A10
    B9 --> C1
    B7 --> C2
    C1 -.->|"Akun terbentuk"| D1
    C2 --> B10
    D1 --> D2
    D2 --> B10
    B10 --> B11
    B11 --> D3
    D3 --> D4
```

> 💡 Alur pada kolom **Sistem** mengikuti urutan pemanggilan fungsi sebenarnya: `login_user` → `show_sidebar` → `input_page` → `metodeMoora` → `insert_akun_user` → `insert_hasil` → `pengumuman_page`.
>
> 🔍 Diagram ini menyajikan **alur utama dokumen** tanpa percabangan, agar perjalanan berkas antar entitas mudah diikuti. Percabangan pada proses autentikasi digambarkan terpisah pada [Flowchart 1](#d-flowchart-1--autentikasi--routing-berbasis-peran).

---

# C. Narasi Alur per Langkah

Tabel berikut adalah padanan tekstual flowmap di atas — tetap terbaca apabila diagram gagal ter-render, dan berguna sebagai acuan penomoran langkah pada laporan.

| No | Entitas | Aktivitas | Dokumen masuk | Dokumen keluar |
|:--:|---|---|---|---|
| 1 | 🏫 Pihak Sekolah | Menghimpun data mentah calon penerima beasiswa | — | Data mentah siswa |
| 2 | 🏫 Pihak Sekolah | Login ke sistem | Kredensial | — |
| 3 | ⚙️ Sistem | Memverifikasi kredensial terhadap tabel `users` | Kredensial | Status sesi & peran |
| 4 | ⚙️ Sistem | Menyediakan berkas template melalui halaman Home | — | `input.csv` (template) |
| 5 | 🏫 Pihak Sekolah | Mengonversi data mentah ke rating kecocokan `1`–`5` secara manual | Data mentah, template | Berkas CSV matriks keputusan |
| 6 | 🏫 Pihak Sekolah | Mengunggah berkas CSV pada halaman Input | Berkas CSV | — |
| 7 | ⚙️ Sistem | Membaca berkas dan menampilkan pratayang data | Berkas CSV | Tabel pratayang |
| 8 | 🏫 Pihak Sekolah | Menekan tombol `Analisis MOORA` | — | Perintah analisis |
| 9 | ⚙️ Sistem | Menghitung normalisasi matriks | Matriks keputusan | Tabel normalisasi |
| 10 | ⚙️ Sistem | Menghitung nilai optimasi `v = w × r` | Matriks normalisasi | Tabel nilai optimasi |
| 11 | ⚙️ Sistem | Menghitung `Yi` sebagai selisih jumlah *benefit* dan *cost* | Matriks optimasi | Nilai `Yi` per alternatif |
| 12 | ⚙️ Sistem | Mengurutkan `Yi` menurun dan memberi nomor peringkat | Nilai `Yi` | Tabel perangkingan |
| 13 | ⚙️ Sistem | Membentuk surel dan menyimpan akun siswa yang belum terdaftar | Daftar alternatif | Baris baru pada `users` |
| 14 | ⚙️ Sistem | Mengosongkan lalu menyimpan hasil perangkingan | Tabel perangkingan | Baris pada `hasil` |
| 15 | 🏫 Pihak Sekolah | Mengunduh berkas hasil | Tabel perangkingan | `output.csv` |
| 16 | 🎒 Siswa | Login memakai akun yang terbentuk otomatis | Kredensial bawaan | Status sesi |
| 17 | ⚙️ Sistem | Mengambil lima peringkat teratas dari tabel `hasil` | Tabel `hasil` | Daftar penerima |
| 18 | 🎒 Siswa | Melihat pengumuman hasil seleksi | — | Daftar penerima beasiswa |

---

# D. Flowchart 1 — Autentikasi & Routing Berbasis Peran

Menggambarkan alur dari pemuatan halaman pertama hingga pemilihan menu, mencakup pengelolaan `st.session_state`.

> 🔖 Sumber: `main.py:83-102`, `main.py:112-135`, `main.py:189-200`

```mermaid
flowchart TD
    START([Halaman dimuat]) --> CEK1{"'loggedIn' ada<br/>di session_state?"}

    CEK1 -->|Tidak| INIT["Inisialisasi session_state<br/>loggedIn = False, role = ''"]
    INIT --> LOGIN[/"Tampilkan halaman login"/]

    CEK1 -->|Ya| CEK2{"loggedIn<br/>bernilai True?"}
    CEK2 -->|Tidak| LOGIN
    CEK2 -->|Ya| LOGOUTBTN["Tampilkan tombol Log Out"]

    LOGIN --> INPUT[/"Pengguna mengisi<br/>surel & kata sandi"/]
    INPUT --> KLIK{"Tombol Login<br/>ditekan?"}
    KLIK -->|Tidak| INPUT
    KLIK -->|Ya| QUERY["login_user:<br/>SELECT * FROM users<br/>WHERE email=? AND password=?"]
    QUERY --> ADA{"Data<br/>ditemukan?"}
    ADA -->|Tidak| ERR[/"Pesan: email dan<br/>password salah"/]
    ERR --> LOGIN
    ADA -->|Ya| SETSESI["loggedIn = True<br/>role = data[0][4]"]
    SETSESI --> LOGOUTBTN

    LOGOUTBTN --> CEKROLE{"role bernilai<br/>'siswa'?"}
    CEKROLE -->|Ya| MENUSISWA["Menu: Home, Pengumuman,<br/>Edit Password"]
    CEKROLE -->|Tidak| MENUSEKOLAH["Menu: Home, Input,<br/>Pengumuman, Edit Password"]

    MENUSISWA --> PILIH{"Menu yang<br/>dipilih"}
    MENUSEKOLAH --> PILIH

    PILIH -->|Home| HOME["show_main_page<br/>siswa_home / sekolah_home"]
    PILIH -->|Input| INPUTPAGE["input_page"]
    PILIH -->|Pengumuman| PENG["pengumuman_page"]
    PILIH -->|Edit Password| EDITPW["edit_password_page"]

    HOME --> SELESAI([Halaman tampil])
    INPUTPAGE --> SELESAI
    PENG --> SELESAI
    EDITPW --> SELESAI
```

> ⚠️ Menu `Input` dipilih dengan pola *else*: setiap peran selain `siswa` memperoleh menu pihak sekolah. Lihat [SRS-F-02](SRS.md#srs-f-02--otorisasi-menu-berbasis-peran).

---

# E. Flowchart 2 — Unggah & Analisis Data

Alur pada halaman Input, dari unggahan berkas sampai hasil tersimpan dan siap diunduh.

> 🔖 Sumber: `main.py:137-161`, `main.py:28-65`

```mermaid
flowchart TD
    START([Halaman Input dibuka]) --> UPLOAD[/"Pengguna memilih<br/>berkas .csv"/]
    UPLOAD --> CEKFILE{"Berkas<br/>terunggah?"}
    CEKFILE -->|Tidak| UPLOAD
    CEKFILE -->|Ya| BACA["pd.read_csv<br/>membaca berkas"]
    BACA --> PRATAYANG[/"Tampilkan seluruh isi<br/>berkas sebagai tabel"/]
    PRATAYANG --> TOMBOL{"Tombol Analisis<br/>MOORA ditekan?"}
    TOMBOL -->|Tidak| PRATAYANG

    TOMBOL -->|Ya| MOORA["metodeMoora dataframe<br/>lihat Flowchart 3"]
    MOORA --> HASIL[/"DataFrame hasil:<br/>Alternatif, Yi, Ranking"/]

    HASIL --> AMBILALT["Ambil kolom alternatif<br/>hasil.iloc[:,0]"]
    AMBILALT --> LOOPMAIL["Untuk setiap nama:<br/>pecah berdasarkan spasi"]
    LOOPMAIL --> CEKKATA{"Jumlah kata<br/>lebih dari 1?"}
    CEKKATA -->|Ya| MAIL2["surel = kata1 + kata2<br/>+ @gmail.com"]
    CEKKATA -->|Tidak| MAIL1["surel = kata1<br/>+ @gmail.com"]
    MAIL2 --> INSERTUSER
    MAIL1 --> INSERTUSER

    INSERTUSER["insert_akun_user:<br/>baca seluruh tabel users"]
    INSERTUSER --> CEKDUP{"Surel sudah<br/>terdaftar?"}
    CEKDUP -->|Ya| SKIP["Lewati, tidak diduplikasi"]
    CEKDUP -->|Tidak| SUSUN["Susun baris akun baru<br/>password 1234, role siswa"]
    SUSUN --> SIMPANUSER[("Simpan ke tabel users")]
    SKIP --> INSERTHASIL
    SIMPANUSER --> INSERTHASIL

    INSERTHASIL["insert_hasil"]
    INSERTHASIL --> HAPUS["DELETE FROM hasil<br/>dan reset AUTOINCREMENT"]
    HAPUS --> SIMPANHASIL[("Simpan ke tabel hasil")]
    SIMPANHASIL --> CEKSIMPAN{"Penyimpanan<br/>berhasil?"}
    CEKSIMPAN -->|Tidak| PESANERR[/"Tampilkan pesan galat"/]
    CEKSIMPAN -->|Ya| PESANOK[/"Behasil Menyimpan data hasil"/]
    PESANOK --> UNDUH[/"Tombol Download Hasil CSV<br/>output.csv"/]
    PESANERR --> AKHIR
    UNDUH --> AKHIR([Selesai])
```

> ⚠️ Tidak ada tahap validasi antara `pd.read_csv` dan `metodeMoora`. Berkas dengan struktur menyimpang menimbulkan *exception* pada tahap perhitungan. Lihat [KI-03](SRS.md#51-daftar-temuan).

---

# F. Flowchart 3 — Algoritma MOORA

Alur inti perhitungan, dengan perulangan digambarkan eksplisit.

> 🔖 Sumber: `moora.py:5-54`

```mermaid
flowchart TD
    START([metodeMoora dipanggil]) --> PISAH["Pisahkan komponen berkas:<br/>data = baris 3 dst, kolom 2 dst<br/>kriteria = baris tajuk<br/>atribut = baris 1<br/>bobot = baris 2"]

    PISAH --> NORMINIT["Siapkan matriks normalisasi<br/>bertipe float64"]
    NORMINIT --> NORMLOOP{"Masih ada sel<br/>i, j?"}
    NORMLOOP -->|Ya| NORMHITUNG["r[i,j] = x[i,j] / √Σ x[:,j]²"]
    NORMHITUNG --> NORMLOOP
    NORMLOOP -->|Tidak| NORMTAMPIL[/"Tabel Normalisasi Data"/]

    NORMTAMPIL --> OPTLOOP{"Masih ada sel<br/>i, j?"}
    OPTLOOP -->|Ya| OPTHITUNG["v[i,j] = r[i,j] × bobot[j]"]
    OPTHITUNG --> OPTLOOP
    OPTLOOP -->|Tidak| OPTTAMPIL[/"Tabel Nilai Optimasi w x r"/]

    OPTTAMPIL --> YIINIT["temp_max = 0<br/>temp_min = 0<br/>untuk setiap alternatif"]
    YIINIT --> YILOOP{"Masih ada<br/>kolom kriteria j?"}
    YILOOP -->|Ya| CEKATR{"atribut[j]<br/>bernilai 1?"}
    CEKATR -->|"Ya · benefit"| TAMBAHMAX["temp_max[i] += v[i,j]"]
    CEKATR -->|"Tidak · cost"| TAMBAHMIN["temp_min[i] += v[i,j]"]
    TAMBAHMAX --> YILOOP
    TAMBAHMIN --> YILOOP
    YILOOP -->|Tidak| HITUNGYI["Yi[i] = temp_max[i] − temp_min[i]"]

    HITUNGYI --> GABUNG["Gabungkan nama alternatif<br/>dengan nilai Yi"]
    GABUNG --> URUT["Urutkan menurun<br/>berdasarkan Yi"]
    URUT --> RANK["Tambahkan kolom Ranking<br/>bernilai 1 sampai n"]
    RANK --> TAMPILRANK[/"Tabel Hasil Perangkingan<br/>Metode MOORA"/]
    TAMPILRANK --> RETURN([Kembalikan df_ranking])
```

### Ringkasan rumus tiap tahap

| Tahap | Rumus | Baris kode |
|---|---|---|
| Normalisasi | `r_ij = x_ij / √(Σ x_ij²)` | `moora.py:14-16` |
| Nilai optimasi | `v_ij = w_j × r_ij` | `moora.py:24-26` |
| Akumulasi *benefit* | `temp_max_i = Σ v_ij` untuk `atribut_j = 1` | `moora.py:36-37` |
| Akumulasi *cost* | `temp_min_i = Σ v_ij` untuk `atribut_j = 0` | `moora.py:38-39` |
| Nilai akhir | `Y_i = temp_max_i − temp_min_i` | `moora.py:42-43` |
| Perangkingan | Urutkan `Y_i` menurun, beri peringkat `1`–`n` | `moora.py:46-49` |

> ℹ️ Pada tahap **Gabungkan**, tabel perangkingan dibentuk langsung dari kolom nama dan kolom `Yi` sehingga masing-masing mempertahankan tipe datanya. Kolom `Yi` bertipe `float64`, sehingga pengurutannya numerik. Lihat [KI-01](SRS.md#51-daftar-temuan) untuk riwayat temuan ini.

---

# G. Flowchart 4 — Publikasi Pengumuman

> 🔖 Sumber: `main.py:67-70`, `main.py:163-178`

```mermaid
flowchart TD
    START([Menu Pengumuman dipilih]) --> AMBIL["hasil_pengumuman:<br/>SELECT nama, ranking<br/>FROM hasil"]
    AMBIL --> CEK{"Data<br/>tersedia?"}

    CEK -->|Tidak| KOSONG[/"Pengumuman Hasil Seleksi Beasiswa<br/>Data hasil seleksi belum keluar"/]
    KOSONG --> AKHIR([Selesai])

    CEK -->|Ya| TEKS[/"Teks pengumuman<br/>hasil seleksi"/]
    TEKS --> DF["Bentuk DataFrame<br/>kolom Nama dan Rangking"]
    DF --> LIMA["Ambil 5 baris teratas<br/>df.head(5)"]
    LIMA --> TABEL[/"Tabel penerima beasiswa"/]
    TABEL --> AKHIR
```

> ℹ️ Halaman ini dapat diakses baik oleh pihak sekolah maupun siswa, dan menampilkan data yang sama bagi keduanya.

---

# H. Diagram Sekuens Sistem

Interaksi antar pelaku dan komponen sepanjang satu siklus seleksi, memakai nama fungsi sebenarnya pada kode.

```mermaid
sequenceDiagram
    autonumber
    actor S as 🏫 Pihak Sekolah
    participant M as main.py
    participant H as home.py
    participant MO as moora.py
    participant DB as 🗄️ beasiswa.db
    actor W as 🎒 Siswa

    S->>M: Isi surel & kata sandi, tekan Login
    M->>DB: login_user(email, password)
    DB-->>M: Baris pengguna
    M->>M: session_state: loggedIn, role
    M->>H: sekolah_home()
    H-->>S: Tabel 1–6 & petunjuk penggunaan
    S->>H: Tekan Download Template CSV
    H-->>S: input.csv

    Note over S: Konversi data mentah<br/>ke rating kecocokan 1–5

    S->>M: Unggah berkas CSV di halaman Input
    M-->>S: Tabel pratayang data
    S->>M: Tekan Analisis MOORA
    M->>MO: metodeMoora(dataframe)
    MO-->>S: Tabel normalisasi
    MO-->>S: Tabel nilai optimasi
    MO-->>S: Tabel perangkingan
    MO-->>M: df_ranking

    M->>M: Bentuk surel dari nama alternatif
    M->>DB: insert_akun_user(username, email)
    DB-->>M: Akun siswa tersimpan
    M->>DB: insert_hasil(dataHasil)
    DB-->>M: Hasil tersimpan
    M-->>S: Tombol Download Hasil CSV

    W->>M: Login dengan akun otomatis
    M->>DB: login_user(email, password)
    DB-->>M: Baris pengguna (role = siswa)
    W->>M: Pilih menu Pengumuman
    M->>DB: hasil_pengumuman()
    DB-->>M: Daftar nama & peringkat
    M-->>W: Tabel 5 penerima teratas
```

---

<div align="center">

[⬆️ Kembali ke atas](#️-flowmap--flowchart) · [📚 Indeks Dokumentasi](README.md) · [📋 SRS](SRS.md) · [🚀 Daftar Fitur](FITUR.md)

</div>
