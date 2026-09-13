<div align="center">

# 📚 Dokumentasi SPK Beasiswa

### Sistem Pendukung Keputusan Penentuan Penerima Beasiswa
**Metode MOORA — SMK Negeri 1 Ciomas, Kabupaten Bogor**

<br/>

![Dokumen](https://img.shields.io/badge/dokumen-4-blue?style=flat-square)
![Bahasa](https://img.shields.io/badge/bahasa-Indonesia-red?style=flat-square)
![Format](https://img.shields.io/badge/format-Markdown-000000?style=flat-square&logo=markdown)

</div>

---

## 📖 Daftar Dokumen

| Dokumen | Isi | Cocok untuk |
|---|---|---|
| **[📋 SRS.md](SRS.md)** | Spesifikasi Kebutuhan Perangkat Lunak dengan struktur **IEEE 830-1998**: pendahuluan, deskripsi umum, kebutuhan fungsional & non-fungsional, kebutuhan data, matriks keterlacakan, serta catatan implementasi | Lampiran laporan, acuan pengembangan, dasar penyusunan kasus uji |
| **[🚀 FITUR.md](FITUR.md)** | Daftar 17 fitur ber-ID (`FT-xx`) dengan status, aktor, halaman, cara pakai, keterbatasan, rujukan kode, dan roadmap | Memahami kemampuan sistem dari sudut pandang pengguna |
| **[🗺️ FLOWMAP.md](FLOWMAP.md)** | Flowmap dokumen bergaya *swimlane* antar entitas, narasi alur 18 langkah, empat flowchart proses, dan diagram sekuens sistem | Memahami alur kerja sistem, bahan presentasi dan laporan |
| **[📖 MANUAL.md](MANUAL.md)** | Buku panduan pemakaian bergambar: 21 screenshot aplikasi yang sesungguhnya, langkah demi langkah untuk pihak sekolah dan siswa, rujukan singkat, dan penyelesaian masalah | Pengguna akhir — petugas sekolah dan siswa |

---

## 🧭 Mulai dari Mana?

| Kebutuhan Anda | Dokumen yang dibaca |
|---|---|
| 🔰 Baru mengenal proyek ini | [README proyek](../README.md) → [FITUR.md](FITUR.md) |
| 🖱️ Akan memakai aplikasinya | [MANUAL.md](MANUAL.md) — panduan bergambar langkah demi langkah |
| 🏫 Ingin tahu apa yang bisa dilakukan sistem | [FITUR.md](FITUR.md) |
| 🔍 Ingin memahami alur kerja sistem | [FLOWMAP.md](FLOWMAP.md) |
| 📐 Menyusun laporan atau skripsi | [SRS.md](SRS.md) + [FLOWMAP.md](FLOWMAP.md) |
| 🧪 Menyusun kasus uji | [SRS bab 3.2](SRS.md#32-kebutuhan-fungsional) — setiap kebutuhan memuat prakondisi, alur, dan pascakondisi |
| 👨‍💻 Akan melanjutkan pengembangan | [SRS bab 5](SRS.md#5-catatan-implementasi--known-issues) + [Roadmap](FITUR.md#️-roadmap) |
| 🗄️ Mencari struktur basis data | [SRS bab 3.3](SRS.md#33-kebutuhan-data) |
| 📥 Mencari ketentuan berkas CSV | [SRS bab 3.3.4](SRS.md#334-spesifikasi-berkas-masukan-csv) atau [README proyek](../README.md#-format-file-input) |

---

## 🔗 Sistem Penomoran

Dokumentasi ini memakai pengenal yang saling merujuk, sehingga setiap kebutuhan dapat dilacak sampai ke baris kode:

| Awalan | Arti | Contoh | Dokumen |
|:---:|---|---|---|
| `SRS-F-xx` | Kebutuhan fungsional | `SRS-F-05` Perhitungan MOORA | [SRS.md](SRS.md#32-kebutuhan-fungsional) |
| `SRS-NF-xx` | Kebutuhan non-fungsional | `SRS-NF-05` Keamanan | [SRS.md](SRS.md#34-kebutuhan-non-fungsional) |
| `FT-xx` | Fitur | `FT-06` Jalankan Analisis MOORA | [FITUR.md](FITUR.md) |
| `KI-xx` | *Known issue* / temuan | `KI-01` Pengurutan `Yi` | [SRS.md](SRS.md#51-daftar-temuan) |
| `BT-xx` / `BF-xx` | Batasan teknis / fungsional | `BT-03` SQLite berkas tunggal | [SRS.md](SRS.md#24-batasan-batasan) |
| `AS-xx` | Asumsi | `AS-02` Data telah dikonversi | [SRS.md](SRS.md#25-asumsi-dan-ketergantungan) |

Alur rujukan: **`SRS-F-xx` → `FT-xx` → `file.py:baris`**, dengan temuan terkait ditandai `KI-xx`. Pemetaan lengkapnya ada pada [matriks keterlacakan](SRS.md#4-matriks-keterlacakan).

---

## ℹ️ Tentang Dokumentasi Ini

- 📅 **Versi 1.0** — disusun berdasarkan pembacaan kode sumber pada commit `e1e6a19`
- 🎯 Seluruh kebutuhan dan fitur dilengkapi rujukan `berkas:baris`, sehingga kesesuaian dokumen dengan kode dapat diperiksa langsung
- 🔍 Fitur yang belum terimplementasi ditandai 📋 dan temuan yang belum terselesaikan dicatat sebagai `KI-xx` — dokumen ini menggambarkan sistem sebagaimana adanya, bukan sebagaimana seharusnya
- 🔄 Bila kode berubah, perbarui rujukan baris dan status pada [matriks keterlacakan](SRS.md#4-matriks-keterlacakan) serta [riwayat revisi](SRS.md#lampiran-a-riwayat-revisi)

---

<div align="center">

[📋 SRS](SRS.md) · [🚀 Daftar Fitur](FITUR.md) · [🗺️ Flowmap](FLOWMAP.md) · [🏠 README Proyek](../README.md)

</div>
