# SIMULASI KODE PROGRAM
simulasi kode program algoritma kompleksitas.
perbandingan linear & binary search pada 7 bahasa pemrograman
(c++, go, java, javascript, php, python, rust)
## Documentation

> Project Structure
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
    ├── rustapp/
    │   ├── helper.rs
    │   └── main.rs
    ├── app.sh
    ├── config.json
    ├── convert_log_to_table.py
    ├── generate_config.py
    ├── Makefile
    └── run.log
> Top-level folders:
    .
    ├── cplus/
    ├── golang/
    ├── java/
    ├── javascript/
    ├── output/
    ├── php/
    ├── py/
    └── rustapp/
Setiap folder berisi kode untuk masing-masing bahasa pemrograman, kecuali folder `output` yang berisi hasil export file .xlsx 
> Top-level files:
    ./
    ├── app.sh
    ├── config.json
    ├── convert_log_to_table.py
    ├── generate_config.py
    ├── Makefile
    └── run.log
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
- `Makefile` : kumpulan kode build dan eksekusi untuk masing-masing bahasa pemrograman.


  
## Installation

enable execute shell script

```bash
chmod +x app.sh
```

build kode program
```bash
./app.sh build
```
    
## Usage

> Step untuk menjalankan app

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

