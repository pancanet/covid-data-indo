# Data jumlah Covid dan Vaksinasi di Indonesia
Data jumlah harian dan total covid 19 di indonesia beserta data vaksinasi berdasarkan web resmi pemerintah indonesia

# Software pendukung
- Python3
- tkinter
- pyinstaller

# Cara menjalankan
- Metode 1
  - Menjalankan program covid.exe (untuk data update harian kasus covid 19) atau vaksin.exe (untuk data update harian vaksinasi covid 19) pada folder dist
- Metode 2 
  - Menjalankan program covid.py (untuk data update harian kasus covid 19) atau vaksin.py (untuk data update harian vaksinasi covid 19) dari terminal ataupun cmd
  - syntax yang digunakan python covid.py atau python3 covid.py

# Edit data 
untuk mengubah data bisa diedit langsung pada program covid.py ataupun vaksin.py

# Mengubah .py menjadi .exe
- Untuk mengubah ekstensi program dapat menjalankan syntax 
- pyinstaller --onefile -w nama_program_nya.py
- Setelah selesai file exe dapat dilihat pada folder dist

# Data API dari pemerintah
- Update kasus covid
  - https://data.covid19.go.id/public/api/update.json
- Update vaksin covid
  - https://data.covid19.go.id/public/api/pemeriksaan-vaksinasi.json
- Data Lab covid
  - https://data.covid19.go.id/public/api/lab.json
- Data kasus covid per provinsi
  - https://data.covid19.go.id/public/api/prov_list.json
- Data penyakit pengikut (data tidak tahu untuk apa tapi)
  - https://data.covid19.go.id/public/api/data.json
