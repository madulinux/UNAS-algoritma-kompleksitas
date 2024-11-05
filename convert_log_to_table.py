import pandas as pd
import re
from datetime import datetime
import argparse
import os
import json

parser = argparse.ArgumentParser(description="Process log data and optionally save to Excel.")
parser.add_argument('--save-excel', action='store_true', help="Save the output to an Excel file.")
parser.add_argument('--sort-by', choices=['binary', 'linear', 'language'], default='language', help="Column to sort by: binary, linear, or language. Default is language.")
args = parser.parse_args()
# Read log data from file
with open('run.log', 'r') as file:
    log_data = file.read()

# Regular expression to parse the log data
pattern = re.compile(r"RUNNING (\w+)\.\.\.\nWarmup:?\s*(\d+)\nJumlah Data:?\s*(\d+)\nTarget:?\s*(\d+)\n\nLinear Search\nIndex: (\d+) \| Time: ([\d.]+) ns\nBinary Search\nIndex: (\d+) \| Time: (\d+) ns")

# Extract data using regex
matches = pattern.findall(log_data)

# Create a DataFrame
columns = ["Language", "Warmup", "Jumlah Data", "Target", "Linear Index", "Linear Time (ns)", "Binary Index", "Binary Time (ns)"]
df = pd.DataFrame(matches, columns=columns)

# Convert numeric columns to appropriate data types
df["Warmup"] = df["Warmup"].astype(int)
df["Jumlah Data"] = df["Jumlah Data"].astype(int)
df["Target"] = df["Target"].astype(int)
df["Linear Index"] = df["Linear Index"].astype(int)
df["Linear Time (ns)"] = df["Linear Time (ns)"].astype(int)
df["Binary Index"] = df["Binary Index"].astype(int)
df["Binary Time (ns)"] = df["Binary Time (ns)"].astype(int)

# Determine the column to sort by
sort_column = {
    'binary': 'Binary Time (ns)',
    'linear': 'Linear Time (ns)',
    'language': 'Language'
}[args.sort_by]

# Sort the DataFrame by the specified column
df = df.sort_values(by=sort_column, ascending=True)

# filename datetime
if args.save_excel:
    # Load data from config.json
    with open('config.json', 'r') as json_file:
        config_data = json.load(json_file)

    # Convert config data to DataFrame
    config_df = pd.DataFrame({
        "Warmup": [config_data["warmup"]],
        "Target": [config_data["target"]],
        "Array": [config_data["arr"]]
    })

    # check output directory
    if not os.path.exists("output"):
        os.makedirs("output")
    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    with pd.ExcelWriter(f"output/{filename}.xlsx") as writer:
        df.to_excel(writer, sheet_name='Log Data', index=False)
        config_df.to_excel(writer, sheet_name='Config Data', index=False)
# Display the table
print(df)