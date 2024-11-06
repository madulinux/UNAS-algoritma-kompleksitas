import json
import random
import argparse

def generate_unique_random_array(size, min_value, max_value):
    if size > (max_value - min_value + 1):
        raise ValueError("Size is too large for the given range of unique values.")
    return random.sample(range(min_value, max_value + 1), size)

def create_json_file_with_random_data(file_path, size, min_value, max_value, warmup = 0):
    arr = generate_unique_random_array(size, min_value, max_value)
    target = arr[len(arr) // 2] # Median
    
    data = {
        "size": size,
        "warmup": warmup,
        "target": target,
        "arr": arr
    }
    
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def update_json_file(file_path, warmup=None, target=None):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    if warmup is not None:
        data['warmup'] = warmup
    if target is not None:
        data['target'] = target
    
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    parser = argparse.ArgumentParser(description="Manage JSON config file.")
    parser.add_argument('--action', choices=['generate', 'update_warmup', 'update_target'], default='generate', help="Action to perform (default: generate)")
    parser.add_argument('--size', type=int, default=1000, help="Size of the array for generation")
    parser.add_argument('--warmup', type=int, default=0, help="New warmup value")
    parser.add_argument('--target', type=int, help="New target value")
    args = parser.parse_args()

    file_path = 'config.json'
    min_value = 1
    max_value = args.size + 1  # Anda dapat menyesuaikan rentang nilai ini

    if args.action == 'generate':
        if args.size is None:
            raise ValueError("Size must be specified for generation.")
        else:
            create_json_file_with_random_data(file_path, args.size, min_value, max_value, args.warmup)
        
    elif args.action == 'update_warmup':
        if args.warmup is None:
            raise ValueError("Warmup value must be specified for update.")
        update_json_file(file_path, warmup=args.warmup)
        print("Nilai warmup telah diganti.")
    elif args.action == 'update_target':
        if args.target is None:
            raise ValueError("Target value must be specified for update.")
        update_json_file(file_path, target=args.target)
        print("Nilai target telah diganti.")

if __name__ == "__main__":
    main()