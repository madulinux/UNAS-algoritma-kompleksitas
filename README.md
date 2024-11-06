# SIMULASI KODE PROGRAM
Simulasi kode program algoritma kompleksitas.
perbandingan linear & binary search pada 7 bahasa pemrograman
(c++, go, java, javascript, php, python, rust)

Content:
- <a href="#documentation">Documentation</a>
- <a href="#flow-program">Flow</a>
- <a href="#installation-and-usage">Instalation & Usage</a>

## Documentation
> Project Structure:
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
> Top-level folders:
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
Setiap folder berisi kode dari masing-masing bahasa pemrograman, untuk setiap bahasa pemrograman menggunakan struktur file yang sama, yaitu `main.*` dan `helper.*`:
- `helper.*` : kode program fungsi linear dan binary search
- `main.*` : kode program utama untuk menjalankan pengujian (linear & binary search), menghitung waktu eksekusi, dan menuliskan hasilnya ke dalam file `run.log`

> Top-level files:
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
Deskripsi untuk masing-masing top-level files:
- `app.sh` : kode shell script untuk menjalankan semua program dalam satu waktu
- `config.json` : file konfigurasi untuk kebutuhan semua program
    ```
    {
        "warmup": 2,
        "target": 35,
        "arr": [119,45,35,41,51,8, ...]
    }
    ```
    - arr: berisi array data yang akan diuji
    - target: target pencarian dari pengujian
    - warmup: jumlah warmup kode sebelum melakukan pengujian
- `generate_config.py` : program python untuk generate konfigurasi `config.json`
- `run.log` : log files untuk menyimpan hasil pengujian dari masing-masing bahasa pemrograman
- `convert_log_to_table.py` : program python untuk menyajikan hasil `run.log` kedalam bentuk table pada tampilan konsole, atau menyimpannya ke dalam file excel.
- `analisis.py` : program python untuk mengkombinasikan data dari semua hasil pengujian (multi dataset) dan melakukan analisis terhadap data tersebut kemudian menyimpannya ke dalam file excel.
- `Makefile` : kumpulan kode build dan eksekusi untuk masing-masing bahasa pemrograman.
- `requirements.txt` : requirement untuk python pandas dan export excel

## Flow Program
berikut adalah flow program untuk menjalankan semua program:

1. Start
    - Jalankan `./app.sh run --loop 1000,2000,3000,4000,5000 --warmup 10 --save --analisis`.
2. Parse Arguments
    - Identifikasi perintah yang dijalankan.
    - Set RUN_MAKE to true.
    - Set LOOP_SIZES to "1000,2000,3000,4000,5000".
    - Set WARMUP to "10".
    - Set SAVE_EXCEL to "--save-excel".
    - Set ANALISIS to true.
3. Run Configurations in Loop
    - Split LOOP_SIZES menjadi individual sizes: 1000, 2000, 3000, 4000, 5000.
    - Untuk setiap size:
        - Update Config
            - Panggil `generate_config.py` dengan nilai SIZE dan WARMUP.
        - Run `Makefile`
            - Eksekusi make run untuk menjalankan semua program dan menuliskan output ke `run.log`.
        - Convert Log to Table
            - Jalankan `convert_log_to_table.py` dengan `--save-excel`.
4. Run Analysis (if --analisis is true)
    - Jalankan `analisis.py` untuk melakukan analisa data, dan mendapatkan hasil dalam bentuk file excel.
5. End
    - Selesai eksekusi `app.sh`.
  
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

## Authors

- [@madulinux](https://www.github.com/madulinux)

