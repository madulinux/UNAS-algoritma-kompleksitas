import random
import time

def linear_search(arr, target):
    for i, v in enumerate(arr):
        if v == target:
            return i 
    return -1

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid 
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def generate_random_array(size, max_value):
    random.seed(time.time())
    return [random.randint(0, max_value - 1) for _ in range(size)]

def generate_random_permutation(n):
    arr = list(range(1, n + 1))
    random.seed(time.time())
    random.shuffle(arr)
    return arr

def format_number_with_thousand_separator(n):
    return "{:,}".format(n).replace(",", ".")