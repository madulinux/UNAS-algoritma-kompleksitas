import json
import os
import time
from helper import linear_search, binary_search

def run_search(search_type, arr, target, warmup):
    if search_type not in ["linear", "binary"]:
        print("Invalid search type. Please use 'linear' or 'binary'.")
        return

    if search_type == "binary":
        # print("Sorting array for binary search")
        arr.sort()

    for _ in range(warmup):
        if search_type == "linear":
            linear_search(arr, target)
        else:
            binary_search(arr, target)

    # Measure time before execution
    start = time.time()

    if search_type == "linear":
        result = linear_search(arr, target)
    else:
        result = binary_search(arr, target)

    # Measure time after execution
    duration = time.time() - start

    print(f"Index: {result} | Time: {int(duration * 1e9)} ns")

def main():
    # read json file
    try:
        with open('../config.json', 'r') as json_file:
            config = json.load(json_file)
    except Exception as e:
        print("Error opening JSON file:", e)
        return

    arr = config['arr']
    target = config['target']
    warmup = config['warmup']

    print("Warmup:", warmup)
    print("Jumlah Data:", len(arr))
    print("Target:", target)
    print()
    print("Linear Search")
    run_search("linear", arr, target, warmup)
    print("Binary Search")
    run_search("binary", arr, target, warmup)
    print()

if __name__ == "__main__":
    main()