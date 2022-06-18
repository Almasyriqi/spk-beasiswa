import streamlit as st
import pandas as pd

def siswa_home():
    st.write("""
        ## Halaman Home
        Selamat Datang di Sistem Pendukung Keputusan Penerimaan Beasiswa SMKN 1 Ciomas Kabupaten Bogor.
        Selamat telah terpilih sebagai calon penerima beasiswa SMKN 1 Ciomas Kabupaten Bogor.
        Silahkan lihat hasil siswa yang terpilih untuk mendapatkan beasiswa pada menu Pengumuman.
        """)

def sekolah_home():
    st.write("""
        ## Halaman Home
        Selamat Datang di Sistem Pendukung Keputusan Penerimaan Beasiswa SMKN 1 Ciomas Kabupaten Bogor.
        Dengan adanya sistem ini diharapkan dapat membantu pihak sekolah SMN 1 Ciomas dalam menentukan
        penerima beasiswa dengan tepat sesuai kriteria yang ditentukan oleh sekolah. 
        Berikut akan disajikan tabel-tabel yang diperlukan dalam sistem ini dan cara penggunaan sistem ini.
        """)
    
    st.write("### Tabel 1 Kriteria")
    tbKriteria = {'Kriteria (C)': ['C1', 'C2', 'C3', 'C4', 'C5'], 
                      'Keterangan': [
                          'Surat Keterangan Tidak Mampu (SKTM)',
                          'Status Anak Dalam Keluarga (SADK)',
                          'Penghasilan Orang Tua (PO)',
                          'Jumlah Tanggungan Orang Tua (JTO)',
                          'Nilai Rata-Rata Raport Semester Terakhir (NRRST)'
                ]}
    dfKriteria = pd.DataFrame(tbKriteria)
    st.dataframe(dfKriteria)
    
    st.write("### Tabel 2 Tingkat Kepentingan Setiap Kriteria")
    tbKepentingan = {'Tingkat Kepentingan': [
                        'Sangat Rendah (SR)',
                        'Rendah (R)',
                        'Cukup (C)',
                        'Tinggi (T)',
                        'Sangat Tinggi (ST)'
                    ], 
                      'Nilai': [1,2,3,4,5]}
    dfKepentingan = pd.DataFrame(tbKepentingan)
    st.dataframe(dfKepentingan, 600)
    
    st.write('### Tabel 3 Nilai Bobot dan Atribut Kriteria')
    tbBobot = {'Kriteria': ['C1', 'C2', 'C3', 'C4', 'C5'],
                   'Bobot': [4,5,3,3,1],
                   'Keterangan': ['Benefit', 'Cost', 'Cost', 'Benefit', 'Benefit']}
        
    dfBobot = pd.DataFrame(tbBobot)
    st.dataframe(dfBobot, 700)
        
    st.write("### Tabel 4 Rating Kecocokan Setiap Alternatif")
    tbRating = {'Rating Kecocokan': [
                        'Sangat Buruk (SB)',
                        'Buruk (B)',
                        'Cukup (C)',
                        'Baik (T)',
                        'Sangat Baik (ST)'
                    ], 
                      'Nilai': [1,2,3,4,5]}
    dfRating = pd.DataFrame(tbRating)
    st.dataframe(dfRating, 600)
        
    st.write("### Tabel 5 Contoh Data Alternatif")
    tbAlternatif = {'Nama': [
            'Abdul Hakim', 'Adi Wiguna', 'Ahmad Zaelani',
            'Desi Ismiyati', 'Dimas Permana', 'Faisal Hidayat',
            'Faridz Dwi Nurfalah', 'Gadis Idhani', 'Hariono Yusuf',
            'Indah Permata Sari'
        ], 'SKTM': [
            'Ada', 'Tidak', 'Ada', 'Ada', 'Ada', 
            'Tidak', 'Ada', 'Ada', 'Tidak', 'Ada' 
        ], 'SADK': [
            'Yatim', 'Yatim', 'Orangtua lengkap', 'Orangtua lengkap', 'Yatim Piatu',
            'Piatu', 'Orangtua lengkap', 'Yatim Piatu', 'Yatim', 'Yatim'
        ], 'PO': [
            '1.000.000<X<=2.000.000', '2.000.000<X<=4.000.000', '1.000.000<X<=2.000.000',
            '1.000.000<X<=2.000.000', 'X<=1.000.000', '2.000.000<X<=4.000.000',
            '1.000.000<X<=2.000.000', '1.000.000<X<=2.000.000', '2.000.000<X<=4.000.000',
            'X<=1.000.000'
        ], 'JTO': [3,2,3,4,3,1,2,3,1,2],
        'NRRST': [80.83, 82.08, 80.66, 78.09, 79.18, 81.09, 78.25, 82.14, 81.71, 81.78]}
    dfAlternatif = pd.DataFrame(tbAlternatif)
    st.dataframe(dfAlternatif, 700)
        
    st.write("### Tabel 6 Contoh Data Siswa Dikonversikan Ke Rating Kecocokan Alternatif")
    tbMatriks = {'Alternatif': [
            'Abdul Hakim', 'Adi Wiguna', 'Ahmad Zaelani',
            'Desi Ismiyati', 'Dimas Permana', 'Faisal Hidayat',
            'Faridz Dwi Nurfalah', 'Gadis Idhani', 'Hariono Yusuf',
            'Indah Permata Sari'
        ], 'C1': [5,1,5,5,5,1,5,5,1,5],
            'C2': [3,3,5,5,2,3,5,2,3,3],
            'C3': [3,5,3,3,2,5,3,3,5,2],
            'C4': [3,2,3,4,3,1,2,3,1,2],
            'C5': [4,4,4,3,3,4,3,4,4,4]}
    dfMatriks = pd.DataFrame(tbMatriks)
    st.dataframe(dfMatriks)
        
    st.write("""
                 ### Cara Penggunaan Sistem
                 1. Download template input data berupa file csv di bawah ini.
                 """)
    dfTemplate = pd.read_csv('./template.csv')
    st.download_button(label='Download Template CSV', data=dfTemplate.to_csv(index=False), file_name="input.csv", mime='text/csv')
        
    st.write("""
                 2. Pada baris Atribut diisikan dengan angka 1 untuk atribut benefit dan angka 0 untuk atribut cost.
                    Atribut benefit merupakan atribut yang jika nilainya lebih tinggi maka lebih baik. Contohnya pada 
                    kriteria nilai rata-rata rapot merupakan atribut benefit karena jika nilainya lebih tinggi maka lebih baik.
                    Sedangkan untuk atribut cost merupakan kebalikan dari atribut benefit yaitu jika nilainya lebih rendah maka lebih baik.
                    Contohnya pada kriteria penghasilan orang tua merupakan atribut cost karena jika nilainya lebih rendah 
                    maka siswa tersebut lebih cocok untuk menerima beasiswa. Pengisian nilai atribut diisi sesuai kolom kriterianya
                    seperti pada template yang disediakan.
                    
                3. Pada baris bobot diisi sesuai dengan aturan pada tabel 2 tingkat kepentingan setiap kriteria.
                    Jadi, bobot diisi dengan range 1 - 5 sesuai kolom kriterianya seperti pada template yang disediakan.
                
                4. Setelah baris bobot, maka selanjutnya merupakan baris alternatif yang diinputkan dengan memasukkan nama siswa
                    dan memasukkan nilai kriteria yang telah dikonversi sesuai pada tabel 4 rating kecocokan setiap alternatif.
                    Pada template pengisian alternatif sama seperti contoh pada tabel 6 (Jika ingin menambah alternatif atau calon penerima beasiswa
                    dapat langsung menambah ke baris selanjutnya, setelah alternatif terakhir).
                    
                5. Jika sudah, dapat masuk ke halaman input untuk upload file csv yang telah diedit sesuai kebutuhan maka sistem akan secara otomatis
                    menghitung menggunakan metode SPK yaitu MOORA. 
                
                6. Langkah tambahan pada saat edit template csv, jika ingin custom kriteria dapat langsung menambah kolom kriteria
                    atau mengurangi kolom kriteria dengan diikuti mengisi nilai atribut, bobot, dan nilai kriteria setiap alternatif 
                    sesuai kriteria yang ditentukan.
                 """)
    st.write("#### Notes : Tidak boleh mengosongi input, mengubah template input atau mengisi input yang tidak sesuai dengan cara penggunaan karena dapat menyebabkan error pada sistem.")