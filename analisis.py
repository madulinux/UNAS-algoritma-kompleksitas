import pandas as pd
import os
from datetime import datetime

# Tentukan folder tempat file .xlsx berada
folder_path = 'output/'

# Buat daftar semua file .xlsx di folder
files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx')]

# order files by name
files.sort()

# Buat list untuk menyimpan data dari setiap file
dataframes = []
config_dataframes = []

# Baca setiap file dan tambahkan ke list
for file in files:
    file_path = os.path.join(folder_path, file)
    try:
        # Read the main data
        df = pd.read_excel(file_path, sheet_name='Log Data')
        dataframes.append(df)
    except ValueError as e:
        print(f"Error reading 'Log Data' from {file}: {e}")
        continue

    try:
        # Read the config data
        config_df = pd.read_excel(file_path, sheet_name='Config Data')
        config_dataframes.append(config_df)
    except ValueError as e:
        print(f"Error reading 'Config Data' from {file}: {e}")
        continue

# Gabungkan semua DataFrame menjadi satu
combined_df = pd.concat(dataframes, ignore_index=True) if dataframes else pd.DataFrame()
combined_config_df = pd.concat(config_dataframes, ignore_index=True) if config_dataframes else pd.DataFrame()

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

    # Pengihtungan time ratio dan time increase
    def calculate_big_o_grouped(average_times, time_column):
        # Group by Language and calculate the ratio of time increase for each step in input size
        average_times['Time Ratio'] = average_times.groupby('Language')[time_column].pct_change().fillna(0) + 1
        # Determine the Big O notation based on the time ratio
        # average_times['Big O'] = average_times['Time Ratio'].apply(
        #     lambda x: 'O(n)' if x > 1 else 'O(1)'
        # )
        
        # jika time ratio lebih besar dari 1 maka 'plus' jika tidak maka 'minus' jika sama dengan 1 maka '.'
        average_times['Increase'] = average_times['Time Ratio'].apply(
            lambda x: '+' if x > 1 else '-' if x < 1 else '.'
        )
        
        # Sort by Language and Jumlah Data
        return average_times.sort_values(by=['Language', 'Jumlah Data'])

    # Calculate time ratio and time increase for Linear and Binary times grouped by Language
    big_o_linear_grouped = calculate_big_o_grouped(average_times_linear, 'Linear Time (ns)')
    big_o_binary_grouped = calculate_big_o_grouped(average_times_binary, 'Binary Time (ns)')

    # # Determine a single Big O conclusion for each language
    # def conclude_big_o(big_o_grouped, time_column):
    #     conclusions = big_o_grouped.groupby('Language').apply(
    #         lambda x: 'O(n)' if (x['Big O'] == 'O(n)').any() else 'O(1)'
    #     ).reset_index(name='Concluded Big O')
    #     return conclusions

    # # Conclude Big O for Linear and Binary times
    # concluded_big_o_linear = conclude_big_o(big_o_linear_grouped, 'Linear Time (ns)')
    # concluded_big_o_binary = conclude_big_o(big_o_binary_grouped, 'Binary Time (ns)')

    # Menyimpan hasil analisis ke file Excel baru
    with pd.ExcelWriter(f"output/analysis_output_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.xlsx") as writer:
        combined_df.to_excel(writer, sheet_name='Combined Data', index=False)
        best_worst_linear.to_excel(writer, sheet_name='Best and Worst Linear', index=False)
        best_worst_binary.to_excel(writer, sheet_name='Best and Worst Binary', index=False)
        big_o_linear_grouped.to_excel(writer, sheet_name='Linear Time Ratio', index=False)
        big_o_binary_grouped.to_excel(writer, sheet_name='Binary Time Ratio', index=False)
        # concluded_big_o_linear.to_excel(writer, sheet_name='Concluded Big O Linear', index=False)
        # concluded_big_o_binary.to_excel(writer, sheet_name='Concluded Big O Binary', index=False)
        if not combined_config_df.empty:
            combined_config_df.to_excel(writer, sheet_name='Combined Config Data', index=False)

    print("Data gabungan dan hasil analisis telah disimpan.")
else:
    print("No valid 'Log Data' found in any Excel files.")