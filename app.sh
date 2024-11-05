#!/bin/bash

# Pastikan Python terinstal dan dapat diakses
if ! command -v python3 &> /dev/null
then
    echo "Python3 tidak ditemukan. Silakan instal Python3 terlebih dahulu."
    exit
fi

# Fungsi untuk menampilkan bantuan
function show_help {
    echo "Penggunaan: $0 [opsi]"
    echo "Opsi:"
    echo "  build             Build ulang kode untuk setiap bahasa pemrograman"
    echo "  run               Menjalankan app dengan opsi save"
    echo "  config            Update konfigurasi pada config.json"
    echo "  log               Menampilkan log output pada console dalam bentuk table"
    echo "  --loop [arr_size]   Loop app dengan konfigurasi data size, contoh: 100,200,300"
    echo "  --save              Export log output ke file Excel"
    echo "  --sort-by [kolom]   Mengurutkan output berdasarkan kolom: binary, linear, atau language"
    echo "  --size [jumlah]    Mengatur jumlah elemen dalam array"
    echo "  --warmup [jumlah]   Mengatur jumlah warmup (opsional)"
    echo "  --target [jumlah]   Mengatur jumlah target"
    echo "  --help              Menampilkan pesan bantuan ini"
}

# Fungsi untuk menjalankan generate_config.py dengan ukuran tertentu dan opsi warmup opsional
function config {
    local size=$1
    local warmup=$2
    echo "Update config.json ukuran $size data dan warmup ${warmup:-tidak disetel}"
    
    if [ -n "$warmup" ]; then
        python3 generate_config.py --size "$size" --warmup "$warmup"
    else
        python3 generate_config.py --size "$size"
    fi
}

# Fungsi untuk menjalankan make run dan convert_log_to_table.py dengan opsi save dan sort-by jika disetel
function runmake {
    echo "Menjalankan app"
    make run

    # Jalankan convert_log_to_table.py dengan opsi save dan sort-by jika ada
    if [ -n "$SAVE_EXCEL" ]; then
        python3 convert_log_to_table.py $SAVE_EXCEL $SORT_BY
    else
        python3 convert_log_to_table.py $SORT_BY
    fi
}

# Variabel untuk menyimpan opsi
SAVE_EXCEL=""
SORT_BY=""
RUN_CONFIG=false
RUN_MAKE=false
BUILD_MAKE=false
CONVERT_LOG=false
SIZE=""
WARMUP=""
TARGET=""
LOOP_SIZES=""

# Parsing argumen
while [[ "$#" -gt 0 ]]; do
    case $1 in
        config) RUN_CONFIG=true ;;
        run) RUN_MAKE=true ;;
        build) BUILD_MAKE=true ;;
        log) CONVERT_LOG=true ;;
        --save) SAVE_EXCEL="--save-excel" ;;  # Hanya digunakan di dalam runmake
        --sort-by) SORT_BY="--sort-by $2"; shift ;;
        --size) SIZE="$2"; shift ;;
        --warmup) WARMUP="$2"; shift ;;
        --target) TARGET="--target $2"; shift ;;
        --loop) LOOP_SIZES="$2"; shift ;;  # Simpan ukuran loop yang dipisahkan koma
        --help) show_help; exit 0 ;;
        *) echo "Opsi tidak dikenal: $1"; show_help; exit 1 ;;
    esac
    shift
done

if [ "$BUILD_MAKE" = true ]; then
    make build-all
fi

# Jalankan generate_config.py jika diminta
if [ "$RUN_CONFIG" = true ]; then
    config "$SIZE" "$WARMUP"
fi

# Jalankan make dan convert_log_to_table.py dengan opsi save dan sort-by jika diminta
if [ "$RUN_MAKE" = true ]; then
    # Periksa apakah opsi loop diatur
    if [ -n "$LOOP_SIZES" ]; then
        # Mengubah IFS untuk memisahkan nilai berdasarkan koma
        IFS=',' read -ra SIZES <<< "$LOOP_SIZES"
        echo "Menjalankan loop dengan ukuran data: ${SIZES[*]}"
        
        # Loop melalui setiap ukuran dalam daftar
        for size in "${SIZES[@]}"; do
            config "$size" "$WARMUP"   # Memanggil fungsi config untuk setiap ukuran dengan warmup opsional
            runmake                    # Memanggil fungsi runmake setelah setiap config
        done
    else
        runmake
    fi
fi
