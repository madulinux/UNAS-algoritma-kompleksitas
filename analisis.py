import pandas as pd
import os
from datetime import datetime

# Tentukan folder tempat file .xlsx berada
folder_path = 'output/'

# Buat daftar semua file .xlsx di folder
files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx')]

# Buat list untuk menyimpan data dari setiap file
dataframes = []
config_dataframes = []

# Baca setiap file dan tambahkan ke list
for file in files:
    file_path = os.path.join(folder_path, file)
    # Load the Excel file
    xls = pd.ExcelFile(file_path)
    
    # Check if 'Log Data' sheet exists
    if 'Log Data' in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name='Log Data')
        dataframes.append(df)
    else:
        print(f"Warning: 'Log Data' sheet not found in {file_path}")

    # Check if 'Config Data' sheet exists
    if 'Config Data' in xls.sheet_names:
        config_df = pd.read_excel(xls, sheet_name='Config Data')
        config_dataframes.append(config_df)
    else:
        print(f"Warning: 'Config Data' sheet not found in {file_path}")

# Gabungkan semua DataFrame menjadi satu
combined_df = pd.concat(dataframes, ignore_index=True) if dataframes else pd.DataFrame()
combined_config_df = pd.concat(config_dataframes, ignore_index=True) if config_dataframes else pd.DataFrame()

# Simpan DataFrame gabungan ke file Excel baru
# combined_df.to_excel('combined_output.xlsx', index=False)

# Analisis data
# Menghitung rata-rata waktu untuk Linear dan Binary berdasarkan jumlah data
if not combined_df.empty:
    average_times_linear = combined_df.groupby(['Jumlah Data', 'Language'])['Linear Time (ns)'].mean().reset_index()
    average_times_binary = combined_df.groupby(['Jumlah Data', 'Language'])['Binary Time (ns)'].mean().reset_index()

    # Menentukan bahasa terbaik dan terburuk untuk Linear Time
    best_worst_linear = average_times_linear.groupby('Jumlah Data', group_keys=False).apply(
        lambda x: pd.Series({
            'Best Language (Linear)': x.loc[x['Linear Time (ns)'].idxmin(), 'Language'],
            'Best Time (Linear)': x['Linear Time (ns)'].min(),
            'Worst Language (Linear)': x.loc[x['Linear Time (ns)'].idxmax(), 'Language'],
            'Worst Time (Linear)': x['Linear Time (ns)'].max(),
            'Average Time (Linear)': x['Linear Time (ns)'].mean()
        })
    ).reset_index()

    # Menentukan bahasa terbaik dan terburuk untuk Binary Time
    best_worst_binary = average_times_binary.groupby('Jumlah Data', group_keys=False).apply(
        lambda x: pd.Series({
            'Best Language (Binary)': x.loc[x['Binary Time (ns)'].idxmin(), 'Language'],
            'Best Time (Binary)': x['Binary Time (ns)'].min(),
            'Worst Language (Binary)': x.loc[x['Binary Time (ns)'].idxmax(), 'Language'],
            'Worst Time (Binary)': x['Binary Time (ns)'].max(),
            'Average Time (Binary)': x['Binary Time (ns)'].mean()
        })
    ).reset_index()

    # Menyimpan hasil analisis ke file Excel baru
    with pd.ExcelWriter(f"output/analysis_output_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.xlsx") as writer:
        combined_df.to_excel(writer, sheet_name='Combined Data', index=False)
        best_worst_linear.to_excel(writer, sheet_name='Best and Worst Linear', index=False)
        best_worst_binary.to_excel(writer, sheet_name='Best and Worst Binary', index=False)
        if not combined_config_df.empty:
            combined_config_df.to_excel(writer, sheet_name='Combined Config Data', index=False)

    print("Data gabungan dan hasil analisis telah disimpan.")
else:
    print("No valid 'Log Data' found in any Excel files.")