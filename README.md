# Content
- <a href="#introduction">Introduction</a>
    - <a href="#tujuan-dan-manfaat">Tujuan dan Manfaat</a>
- <a href="#documentation">Documentation</a>
    - <a href="#project-structure">Project Structure</a>
- <a href="#flow-program">Flow</a>
- <a href="#installation-and-usage">Instalation & Usage</a>

# Introduction
aplikasi ini dibuat untuk membandingkan kompleksitas dua algoritma pencaria `Linear Search` dan `Binary Search` dalam berbagai bahasa pemrograman. Aplikasi ini tidak hanya menguji algoritma, tetapi juga membantu kita menganalisis waktu eksekusi untuk berbagai ukuran dataset dan perbandingan antar bahasa pemrograman.
Simulasi kode program algoritma kompleksitas.

## Tujuan dan Manfaat
Tujuan utama dari proyek ini adalah untuk melakukan perbandingan performa antara algoritma pencarian Linear Search dan Binary Search menggunakan dataset yang bervariasi, dengan mengukur waktu eksekusi pada tujuh bahasa pemrograman yang berbeda: C++, Go, Java, JavaScript, PHP, Python, dan Rust.
<br/><br/>
Selain itu, proyek ini bertujuan untuk menunjukkan bagaimana kompleksitas algoritma ini berperilaku pada berbagai ukuran data, serta bagaimana perbedaan implementasi dalam masing-masing bahasa pemrograman mempengaruhi hasil eksekusi.
<br/><br/>
Pada akhirnya diharapkan aplikasi ini dapat mempermudah membandingkan performa algoritma pencarian Linear dan Binary Search, serta mengidentifikasi bagaimana bahasa pemrograman yang berbeda mempengaruhi waktu eksekusi. Ini memberikan gambaran yang lebih jelas mengenai perbandingan kompleksitas algoritma dalam konteks praktis.

## Documentation
### Project Structure
Berikut adalah gambaran umum dari struktur proyek yang digunakan
```
./
├── cplus/
├── golang/
├── java/
├── javascript/
├── php/
├── py/
├── rustapp/
├── analisis.py
├── app.sh
├── config.json
├── convert_log_to_table.py
├── generate_config.py
├── Makefile
├── requirements.txt
└── run.log
```
#### Top-level folders:
Proyek ini terdiri dari beberapa folder yang masing-masing berisi kode untuk bahasa pemrograman
```
./
├── cplus/
│   ├── helper.cpp
│   └── main.cpp
├── golang/
│   ├── helper.go
│   └── main.go
├── java/
│   ├── Helper.java
│   └── Main.java
├── javascript/
│   ├── helper.js
│   └── main.js
├── php/
│   ├── helper.php
│   └── main.php
├── py/
│   ├── helper.py
│   └── main.py
└── rustapp/
    └── src/
        ├── helper.rs
        └── main.rs
```
Setiap folder memiliki dua file utama:
- `helper.*` : berisi kode fungsi program implementasi Linear Search dan Binary Search.
- `main.*` : kode program utama untuk menjalankan pengujian (linear & binary search), menghitung waktu eksekusi, dan mencatat hasilnya ke dalam file `run.log`

#### Top-level files:
Selain folder kode program, ada beberapa file utama yang berfungsi untuk konfigurasi dan pengolahan data, seperti config.json untuk pengaturan array yang diuji dan target pencarian, serta run.log yang menyimpan hasil pengujian.
```
./
├── analisis.py
├── app.sh
├── config.json
├── convert_log_to_table.py
├── generate_config.py
├── Makefile
├── requirements.txt
└── run.log
```
berikut penjelasan untuk masing-masing top-level files:
- `requirements.txt` : requirement untuk python pandas dan export excel
- `app.sh` : kode shell script untuk menjalankan semua program dalam satu waktu
- `Makefile` : kumpulan kode build dan eksekusi untuk masing-masing bahasa pemrograman.
- `config.json` : file konfigurasi untuk dataset pengujian
    ```
    {
        "warmup": 2,
        "target": 35,
        "arr": [119,45,35,41,51,8, ...]
    }
    ```
    - arr: berisi array data yang akan diuji
    - target: target pencarian dari pengujian
    - warmup: jumlah warm-up yang dilakukan sebelum pengujian dimulai
- `generate_config.py` : program python untuk generate konfigurasi `config.json`
- `run.log` : log files untuk menyimpan hasil pengujian dari masing-masing bahasa pemrograman
- `convert_log_to_table.py` : program python untuk menyajikan hasil `run.log` kedalam bentuk table pada tampilan konsole, atau menyimpannya ke dalam file excel.
- `analisis.py` : program python untuk mengkombinasikan data dari semua hasil pengujian (multi dataset) dan melakukan analisis terhadap data tersebut kemudian menyimpannya ke dalam file excel.

## Flow Program
berikut adalah flow program untuk menjalankan semua program:

1. Start
    - Jalankan script `app.sh` dengan parameter yang diinginkan, misal:  `./app.sh run --loop 1000,2000,3000,4000,5000 --warmup 10 --save --analisis`. untuk mengetahui lebih lanjut tentang cata penggunaan lihat  <a href="#installation-and-usage">disini</a>
2. Parse Arguments
    - Identifikasi perintah yang dijalankan.
    - dengan opsi `--loop 1000,2000,3000,4000,5000`, aplikasi akan menguji lima ukuran dataset: 1000, 2000, 3000, 4000, dan 5000 elemen.
    - Set banyaknya iterasi warm-up dari opsi `--warmup 10` untuk menghindari efek optimasi cache yang mungkin memengaruhi hasil pengujian.
    - Set `--save` agar aplikasi melakukan export hasil hari pengujian kedalam format excel.
    - Set `--analisis` agar setelah melakukan pengujian pada semua dataset, aplikasi langsung melakukan analisa data..
3. Run Configurations in Loop
    - Split LOOP_SIZES menjadi individual sizes: 1000, 2000, 3000, 4000, 5000.
    - Untuk setiap size melakukan perulangan:
        - Update file konfigurasi
            - menjalankan `generate_config.py` dengan nilai SIZE dan WARMUP yang ditentukan, kemudian melakukan update pada file `config.json` untuk digunakan sebagai data pengujian.
        - Jalankan Pengujian
            - Eksekusi `make run` untuk menguji algoritma pencarian dengan menghitung waktu eksekusi untuk setiap bahasa pemrograman,
            - Setiap bahasa pemrograman mencatat hasil pengujian dalam file `run.log`
        - Penyajian Data Hasil Pengujian
            - Setelah pengujian selesai, kemudian jalankan `convert_log_to_table.py` untuk mengonversi hasil log tersebut menjadi format tabel."
            - Argumen `--save` akan membuat program mengeksport hasil log menjadi file excel (`.xlsx`).
4. Pengumpulan & Analisis Hasil Pengujian
    - Mengumpulkan semua hasil pengujian kedalam satu file
    - Melakukan analisa dari semua hasil pengujian, dan menyajikannya dalam bentuk file excel
5. End
  
## Installation and Usage
### Instalation

clone source code
```bash
git clone https://github.com/madulinux/UNAS-algoritma-kompleksitas.git
```

install python export data requirements
```bash
pip install -r requirements.txt
```

enable execute shell script
```bash
chmod +x app.sh
```

build kode program
```bash
./app.sh build
```
    
### Usage
Step untuk menjalankan app

melihat helper untuk menjalankan program
```bash
./app.sh --help
```

untuk generate konfigurasi
```bash
./app.sh config --size 1000 --warmup 5
```

untuk menjalankan pengujian
```bash
./app.sh run
```

menjalankan pengujian multi dataset
```bash
./app.sh run --loop 100,200,300
```

# EXAMPLE





## Authors

- [@madulinux](https://www.github.com/madulinux)

