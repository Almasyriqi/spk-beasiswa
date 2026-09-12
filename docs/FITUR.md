<div align="center">

# 🚀 Daftar Fitur

### SPK Beasiswa — Metode MOORA
**SMK Negeri 1 Ciomas, Kabupaten Bogor**

<br/>

![Fitur](https://img.shields.io/badge/total%20fitur-17-blue?style=flat-square)
![Terimplementasi](https://img.shields.io/badge/terimplementasi-14-success?style=flat-square)
![Sebagian](https://img.shields.io/badge/sebagian-1-orange?style=flat-square)
![Belum](https://img.shields.io/badge/belum-2-lightgrey?style=flat-square)

</div>

---

## 📑 Daftar Isi

| | |
|---|---|
| [📊 Ringkasan Status](#-ringkasan-status) | [🧮 Perhitungan MOORA](#-perhitungan-moora) |
| [🧭 Matriks Fitur × Peran](#-matriks-fitur--peran) | [📢 Publikasi Hasil](#-publikasi-hasil) |
| [🔐 Autentikasi & Sesi](#-autentikasi--sesi) | [👤 Manajemen Akun](#-manajemen-akun) |
| [📥 Manajemen Data](#-manajemen-data) | [⚙️ Infrastruktur & Pendukung](#️-infrastruktur--pendukung) |
| [🗺️ Roadmap](#️-roadmap) | [🔗 Keterkaitan Dokumen](#-keterkaitan-dokumen) |

> 📎 **Dokumen terkait:** [SRS](SRS.md) · [Flowmap & Flowchart](FLOWMAP.md) · [README Proyek](../README.md)

---

## 📊 Ringkasan Status

Dokumen ini memandang sistem dari sudut pandang **pengguna**: apa yang dapat dilakukan, oleh siapa, dan di halaman mana. Rumusan formal tiap kebutuhan beserta prakondisi dan pascakondisinya berada pada [SRS bab 3.2](SRS.md#32-kebutuhan-fungsional).

| Lambang | Arti | Jumlah |
|:--:|---|:--:|
| ✅ | **Tersedia** — fitur dapat dipakai sebagaimana dijelaskan | 14 |
| ⚠️ | **Sebagian** — fitur dapat dipakai namun memiliki keterbatasan yang diketahui | 1 |
| 📋 | **Belum tersedia** — fitur direncanakan, belum diimplementasikan | 2 |
| | **Total** | **17** |

### Sebaran fitur per modul

| Modul | Jumlah | ✅ | ⚠️ | 📋 |
|---|:--:|:--:|:--:|:--:|
| 🔐 Autentikasi & Sesi | 3 | 3 | — | — |
| 📥 Manajemen Data | 3 | 2 | — | 1 |
| 🧮 Perhitungan MOORA | 4 | 3 | 1 | — |
| 📢 Publikasi Hasil | 3 | 3 | — | — |
| 👤 Manajemen Akun | 3 | 2 | — | 1 |
| ⚙️ Infrastruktur | 1 | 1 | — | — |

---

## 🧭 Matriks Fitur × Peran

| ID | Fitur | 🏫 Pihak Sekolah | 🎒 Siswa | Status |
|:--:|---|:--:|:--:|:--:|
| FT-01 | Login | ✅ | ✅ | ✅ |
| FT-02 | Menu sesuai peran | ✅ | ✅ | ✅ |
| FT-03 | Logout | ✅ | ✅ | ✅ |
| FT-04 | Unggah berkas CSV | ✅ | — | ✅ |
| FT-05 | Unduh template CSV | ✅ | — | ✅ |
| FT-06 | Jalankan analisis MOORA | ✅ | — | ✅ |
| FT-07 | Lihat tabel tiap tahap perhitungan | ✅ | — | ✅ |
| FT-08 | Lihat tabel perangkingan | ✅ | — | ⚠️ |
| FT-09 | Simpan hasil ke basis data | ✅ | — | ✅ |
| FT-10 | Lihat pengumuman penerima | ✅ | ✅ | ✅ |
| FT-11 | Akun siswa dibuat otomatis | ✅ | — | ✅ |
| FT-12 | Unduh hasil perangkingan | ✅ | — | ✅ |
| FT-13 | Ubah kata sandi | ✅ | ✅ | ✅ |
| FT-14 | Kriteria dinamis lewat CSV | ✅ | — | ✅ |
| FT-15 | Validasi berkas CSV | ✅ | — | 📋 |
| FT-16 | Manajemen akun pengguna | ✅ | — | 📋 |
| FT-17 | Referensi kriteria & petunjuk penggunaan | ✅ | — | ✅ |

---

## 🔐 Autentikasi & Sesi

### FT-01 · Login

| | |
|---|---|
| **Deskripsi** | Masuk ke sistem dengan surel dan kata sandi. Sistem mengenali peran pengguna dari kolom `role` pada tabel `users` |
| **Aktor** | Pihak Sekolah, Siswa |
| **Halaman** | Login (halaman awal) |
| **Cara pakai** | Isi surel dan kata sandi, lalu tekan tombol `Login`. Bila kredensial salah, tampil pesan `email dan password salah` |
| **Status** | ✅ Tersedia |
| **Kebutuhan** | [SRS-F-01](SRS.md#srs-f-01--autentikasi-pengguna) |
| **Rujukan Kode** | `main.py:13-16`, `main.py:120-135` |

### FT-02 · Menu Sesuai Peran

| | |
|---|---|
| **Deskripsi** | Menu samping menyesuaikan diri dengan peran pengguna. Pihak sekolah memperoleh menu `Input`, siswa tidak |
| **Aktor** | Pihak Sekolah, Siswa |
| **Halaman** | Menu samping (seluruh halaman) |
| **Cara pakai** | Otomatis setelah login. Pihak sekolah: Home · Input · Pengumuman · Edit Password. Siswa: Home · Pengumuman · Edit Password |
| **Status** | ✅ Tersedia |
| **Kebutuhan** | [SRS-F-02](SRS.md#srs-f-02--otorisasi-menu-berbasis-peran) |
| **Rujukan Kode** | `main.py:83-102` |

### FT-03 · Logout

| | |
|---|---|
| **Deskripsi** | Mengakhiri sesi dan kembali ke halaman login |
| **Aktor** | Pihak Sekolah, Siswa |
| **Halaman** | Menu samping |
| **Cara pakai** | Tekan tombol `Log Out` di bagian bawah menu samping |
| **Status** | ✅ Tersedia |
| **Keterbatasan** | Nilai `role` tidak dibersihkan dari sesi ([KI-05](SRS.md#51-daftar-temuan)) |
| **Kebutuhan** | [SRS-F-03](SRS.md#srs-f-03--mengakhiri-sesi-logout) |
| **Rujukan Kode** | `main.py:112-118` |

---

## 📥 Manajemen Data

### FT-04 · Unggah Berkas CSV

| | |
|---|---|
| **Deskripsi** | Memasukkan matriks keputusan — kriteria, atribut, bobot, dan nilai setiap alternatif — melalui berkas CSV |
| **Aktor** | Pihak Sekolah |
| **Halaman** | Input |
| **Cara pakai** | Tekan area `Choose CSV file`, pilih berkas berekstensi `.csv`. Isi berkas langsung tampil sebagai pratayang untuk diperiksa sebelum dianalisis |
| **Status** | ✅ Tersedia |
| **Keterbatasan** | Belum ada pemeriksaan struktur berkas; berkas yang tidak sesuai memicu galat ([KI-03](SRS.md#51-daftar-temuan)) |
| **Kebutuhan** | [SRS-F-04](SRS.md#srs-f-04--unggah-matriks-keputusan-berkas-csv) |
| **Rujukan Kode** | `main.py:137-143` |

### FT-05 · Unduh Template CSV

| | |
|---|---|
| **Deskripsi** | Mengunduh berkas contoh berisi struktur yang benar beserta sepuluh data alternatif sebagai acuan pengisian |
| **Aktor** | Pihak Sekolah |
| **Halaman** | Home |
| **Cara pakai** | Tekan tombol `Download Template CSV`. Berkas tersimpan dengan nama `input.csv` |
| **Status** | ✅ Tersedia |
| **Kebutuhan** | [SRS-F-11](SRS.md#srs-f-11--unduh-template-dan-hasil) |
| **Rujukan Kode** | `home.py:101-106`, `template.csv` |

### FT-15 · Validasi Berkas CSV

| | |
|---|---|
| **Deskripsi** | Pemeriksaan otomatis atas kelengkapan dan kesesuaian berkas sebelum analisis dijalankan, dengan pesan kesalahan yang mudah dipahami |
| **Aktor** | Pihak Sekolah |
| **Halaman** | Input |
| **Status** | 📋 Belum tersedia |
| **Kebutuhan** | [SRS-F-14](SRS.md#srs-f-14--validasi-struktur-dan-isi-berkas-csv) |
| **Catatan** | Kondisi saat ini dinyatakan terbuka pada `home.py:133`: berkas yang tidak sesuai ketentuan dapat menyebabkan galat pada sistem |

---

## 🧮 Perhitungan MOORA

### FT-06 · Jalankan Analisis MOORA

| | |
|---|---|
| **Deskripsi** | Menjalankan seluruh tahap metode MOORA atas data yang diunggah: normalisasi, pembobotan, perhitungan nilai `Yi`, dan perangkingan |
| **Aktor** | Pihak Sekolah |
| **Halaman** | Input |
| **Cara pakai** | Setelah berkas terunggah, tekan tombol `Analisis MOORA`. Sistem sekaligus membuat akun siswa (FT-11) dan menyimpan hasil (FT-09) |
| **Status** | ✅ Tersedia |
| **Kebutuhan** | [SRS-F-05](SRS.md#srs-f-05--perhitungan-metode-moora) |
| **Rujukan Kode** | `main.py:144-160`, `moora.py:5-43` |

### FT-07 · Tabel Tiap Tahap Perhitungan

| | |
|---|---|
| **Deskripsi** | Menampilkan tiga tabel berurutan — `Normalisasi Data`, `Nilai Optimasi (w x r)`, dan `Hasil Perangkingan Metode MOORA` — sehingga hasil dapat ditelusuri dan dipertanggungjawabkan |
| **Aktor** | Pihak Sekolah |
| **Halaman** | Input |
| **Cara pakai** | Tabel tampil otomatis setelah tombol `Analisis MOORA` ditekan |
| **Status** | ✅ Tersedia |
| **Kebutuhan** | [SRS-F-06](SRS.md#srs-f-06--penyajian-tabel-setiap-tahap-perhitungan) |
| **Rujukan Kode** | `moora.py:17-18`, `moora.py:27-28`, `moora.py:53-54` |

### FT-08 · Tabel Perangkingan

| | |
|---|---|
| **Deskripsi** | Menampilkan daftar alternatif terurut menurun berdasarkan nilai `Yi`, dilengkapi kolom nomor peringkat |
| **Aktor** | Pihak Sekolah |
| **Halaman** | Input |
| **Status** | ⚠️ Sebagian |
| **Keterbatasan** | Nilai `Yi` tersimpan sebagai teks akibat penggabungan array, sehingga pengurutan berpotensi leksikografis dan peringkat dapat salah pada data tertentu ([KI-01](SRS.md#51-daftar-temuan)) |
| **Kebutuhan** | [SRS-F-07](SRS.md#srs-f-07--perangkingan-alternatif) |
| **Rujukan Kode** | `moora.py:46-56` |

### FT-14 · Kriteria Dinamis

| | |
|---|---|
| **Deskripsi** | Jumlah kriteria dapat ditambah maupun dikurangi hanya dengan menyunting berkas CSV — tanpa mengubah kode sistem |
| **Aktor** | Pihak Sekolah |
| **Halaman** | Input (melalui berkas CSV) |
| **Cara pakai** | Tambah atau kurangi kolom kriteria pada berkas, lalu lengkapi nilai pada baris `Atribut` dan `Bobot` beserta nilai setiap alternatif |
| **Status** | ✅ Tersedia |
| **Kebutuhan** | [SRS-F-13](SRS.md#srs-f-13--kriteria-dinamis) |
| **Rujukan Kode** | `moora.py:7-10`, `moora.py:14-16`, `moora.py:34-39` |

---

## 📢 Publikasi Hasil

### FT-09 · Simpan Hasil ke Basis Data

| | |
|---|---|
| **Deskripsi** | Menyimpan tabel perangkingan ke tabel `hasil` agar dapat ditampilkan pada halaman Pengumuman |
| **Aktor** | Sistem, dipicu oleh Pihak Sekolah |
| **Halaman** | Input (berjalan otomatis) |
| **Cara pakai** | Berjalan sendiri setelah analisis. Tampil pesan `Behasil Menyimpan data hasil` bila berhasil |
| **Status** | ✅ Tersedia |
| **Keterbatasan** | Hasil sebelumnya terhapus; tidak ada riwayat seleksi ([KI-06](SRS.md#51-daftar-temuan)) |
| **Kebutuhan** | [SRS-F-09](SRS.md#srs-f-09--penyimpanan-hasil-seleksi) |
| **Rujukan Kode** | `main.py:57-65`, `main.py:160` |

### FT-10 · Lihat Pengumuman Penerima

| | |
|---|---|
| **Deskripsi** | Menampilkan lima alternatif peringkat teratas sebagai penerima beasiswa. Bila belum ada hasil, tampil keterangan bahwa hasil seleksi belum keluar |
| **Aktor** | Pihak Sekolah, Siswa |
| **Halaman** | Pengumuman |
| **Cara pakai** | Pilih menu `Pengumuman` pada menu samping |
| **Status** | ✅ Tersedia |
| **Keterbatasan** | Jumlah penerima dipatok lima pada kode ([KI-07](SRS.md#51-daftar-temuan)) |
| **Kebutuhan** | [SRS-F-10](SRS.md#srs-f-10--publikasi-pengumuman-hasil-seleksi) |
| **Rujukan Kode** | `main.py:67-70`, `main.py:163-178` |

### FT-12 · Unduh Hasil Perangkingan

| | |
|---|---|
| **Deskripsi** | Mengunduh tabel perangkingan lengkap sebagai berkas CSV untuk dokumentasi atau pengolahan lanjutan |
| **Aktor** | Pihak Sekolah |
| **Halaman** | Input |
| **Cara pakai** | Setelah analisis selesai, tekan tombol `Download Hasil CSV`. Berkas tersimpan dengan nama `output.csv` |
| **Status** | ✅ Tersedia |
| **Kebutuhan** | [SRS-F-11](SRS.md#srs-f-11--unduh-template-dan-hasil) |
| **Rujukan Kode** | `main.py:161` |

---

## 👤 Manajemen Akun

### FT-11 · Akun Siswa Dibuat Otomatis

| | |
|---|---|
| **Deskripsi** | Setiap alternatif pada berkas CSV memperoleh akun siswa secara otomatis, tanpa pendaftaran manual dan tanpa duplikasi |
| **Aktor** | Sistem, dipicu oleh Pihak Sekolah |
| **Halaman** | Input (berjalan otomatis) |
| **Aturan pembentukan** | Surel: dua kata pertama nama digabung tanpa spasi + `@gmail.com` · Kata sandi: `1234` · Peran: `siswa` |
| **Contoh** | `Abdul Hakim` → `AbdulHakim@gmail.com` · `Indah Permata Sari` → `IndahPermata@gmail.com` |
| **Status** | ✅ Tersedia |
| **Keterbatasan** | Nama dengan dua kata pertama identik berpotensi bertabrakan ([KI-04](SRS.md#51-daftar-temuan)) |
| **Kebutuhan** | [SRS-F-08](SRS.md#srs-f-08--pembuatan-akun-siswa-otomatis) |
| **Rujukan Kode** | `main.py:28-55`, `main.py:147-159` |

### FT-13 · Ubah Kata Sandi

| | |
|---|---|
| **Deskripsi** | Mengganti kata sandi sendiri setelah memverifikasi kata sandi lama — terutama diperlukan siswa untuk menggantikan kata sandi bawaan `1234` |
| **Aktor** | Pihak Sekolah, Siswa |
| **Halaman** | Edit Password |
| **Cara pakai** | Isi surel, kata sandi saat ini, dan kata sandi baru, lalu tekan tombol `Edit` |
| **Status** | ✅ Tersedia |
| **Keterbatasan** | Kolom surel diisi manual, tidak diambil dari sesi aktif. Kata sandi disimpan sebagai teks biasa ([KI-02](SRS.md#51-daftar-temuan)) |
| **Kebutuhan** | [SRS-F-12](SRS.md#srs-f-12--ubah-kata-sandi) |
| **Rujukan Kode** | `main.py:18-26`, `main.py:180-187` |

### FT-16 · Manajemen Akun Pengguna

| | |
|---|---|
| **Deskripsi** | Antarmuka bagi pihak sekolah untuk melihat, menambah, menyunting, dan menghapus akun pengguna |
| **Aktor** | Pihak Sekolah |
| **Status** | 📋 Belum tersedia |
| **Kebutuhan** | [SRS-F-15](SRS.md#srs-f-15--manajemen-akun-pengguna) |
| **Catatan** | Saat ini akun pihak sekolah dibuat langsung pada berkas basis data, tanpa antarmuka |

---

## ⚙️ Infrastruktur & Pendukung

### FT-17 · Referensi Kriteria & Petunjuk Penggunaan

| | |
|---|---|
| **Deskripsi** | Halaman Home pihak sekolah memuat enam tabel referensi dan petunjuk penggunaan berurutan, sehingga pengguna tidak perlu dokumentasi terpisah saat mengisi berkas |
| **Aktor** | Pihak Sekolah |
| **Halaman** | Home |
| **Isi** | Tabel 1 Kriteria · Tabel 2 Tingkat Kepentingan · Tabel 3 Bobot & Atribut · Tabel 4 Rating Kecocokan · Tabel 5 Contoh Data Alternatif · Tabel 6 Contoh Konversi ke Rating · Petunjuk penggunaan enam langkah |
| **Status** | ✅ Tersedia |
| **Keterbatasan** | Singkatan label rating kecocokan tidak konsisten ([KI-09](SRS.md#51-daftar-temuan)) |
| **Kebutuhan** | [SRS-F-16](SRS.md#srs-f-16--penyajian-referensi-kriteria-dan-petunjuk-penggunaan) |
| **Rujukan Kode** | `home.py:21-133` |

### Fitur pendukung lain

| Fitur | Keterangan | Berkas |
|---|---|---|
| 🌙 **Tema gelap** | Tema gelap aktif sebagai bawaan aplikasi | `.streamlit/config.toml` |
| 🐳 **Dev Container** | Pemasangan dependensi otomatis dan penerusan porta `8501`, siap untuk GitHub Codespaces maupun VS Code Dev Containers | `.devcontainer/devcontainer.json` |
| 📊 **Berkas template** | Contoh berkas masukan berisi struktur benar dan sepuluh data alternatif | `template.csv` |
| 🗄️ **Basis data siap pakai** | Berkas basis data disertakan pada repositori, memuat akun pihak sekolah sehingga aplikasi dapat langsung dicoba | `beasiswa.db` |

---

## 🗺️ Roadmap

Fitur berikut belum tersedia, diurutkan menurut prioritas penanganan. Urutan mengikuti [SRS bab 5.2](SRS.md#52-urutan-penanganan-yang-disarankan).

### 🔴 Prioritas tinggi

| Fitur | Alasan | Rujukan |
|---|---|---|
| **Perbaikan pengurutan peringkat** | Satu-satunya temuan yang dapat membuat *hasil* sistem salah. Nilai `Yi` perlu dipertahankan sebagai tipe numerik agar pengurutan benar | [KI-01](SRS.md#51-daftar-temuan) |
| **Penyimpanan kata sandi ter-*hash*** | Kata sandi saat ini tersimpan sebagai teks biasa dan terbaca bila berkas basis data bocor. Memerlukan migrasi data yang sudah ada | [KI-02](SRS.md#51-daftar-temuan) |

### 🟠 Prioritas sedang

| Fitur | Alasan | Rujukan |
|---|---|---|
| **Validasi berkas CSV** | Mencegah galat teknis tampil kepada pengguna dan memberi petunjuk perbaikan yang jelas | [FT-15](#ft-15--validasi-berkas-csv), [KI-03](SRS.md#51-daftar-temuan) |
| **Surel siswa yang dijamin unik** | Mencegah dua siswa dengan dua kata pertama nama yang sama hanya memperoleh satu akun | [KI-04](SRS.md#51-daftar-temuan) |
| **Pemaksaan penggantian kata sandi bawaan** | Seluruh siswa memiliki kata sandi awal yang sama, sehingga siapa pun dapat masuk ke akun siswa lain | [SRS-NF-05](SRS.md#srs-nf-05--keamanan) |

### 🟡 Prioritas rendah

| Fitur | Alasan | Rujukan |
|---|---|---|
| **Riwayat seleksi antar periode** | Hasil analisis sebelumnya kini terhapus, sehingga perbandingan antar periode tidak dimungkinkan | [KI-06](SRS.md#51-daftar-temuan) |
| **Kuota penerima yang dapat diatur** | Jumlah penerima dipatok lima pada kode; sekolah mungkin perlu jumlah lain | [KI-07](SRS.md#51-daftar-temuan) |
| **Manajemen akun pengguna** | Menghilangkan kebutuhan menyunting berkas basis data secara langsung | [FT-16](#ft-16--manajemen-akun-pengguna) |
| **Pencantuman `pandas` & `numpy` pada `requirements.txt`** | Keduanya kini ikut sebagai dependensi transitif Streamlit — rapuh bila versi Streamlit diganti | [KI-08](SRS.md#51-daftar-temuan) |
| **Konversi otomatis data mentah ke rating** | Konversi data mentah siswa ke skala `1`–`5` kini dilakukan manual dan rawan keliru | — |
| **Perbaikan label rating kecocokan** | Singkatan `(T)` dan `(ST)` tidak sesuai untuk "Baik" dan "Sangat Baik" | [KI-09](SRS.md#51-daftar-temuan) |

---

## 🔗 Keterkaitan Dokumen

| Dokumen | Hubungan dengan dokumen ini |
|---|---|
| [📋 SRS](SRS.md) | Setiap `FT-xx` di sini mengacu ke satu atau lebih `SRS-F-xx`. SRS memuat prakondisi, alur, dan pascakondisi formal tiap kebutuhan |
| [🗺️ Flowmap](FLOWMAP.md) | Menggambarkan urutan pemakaian fitur-fitur ini dalam satu alur proses utuh |
| [📖 README](../README.md) | Ringkasan fitur untuk pembaca yang baru mengenal proyek |

---

<div align="center">

[⬆️ Kembali ke atas](#-daftar-fitur) · [📚 Indeks Dokumentasi](README.md) · [📋 SRS](SRS.md) · [🗺️ Flowmap](FLOWMAP.md)

</div>
