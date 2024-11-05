mod helper;

use std::fs;
use std::time::Instant;

#[derive(serde::Deserialize)]
struct Config {
    warmup: i32,
    target: i32,
    arr: Vec<i32>,
}

fn main() {
    let data = fs::read_to_string("../config.json").expect("Unable to read file");
    let config: Config = serde_json::from_str(&data).expect("JSON was not well-formatted");

    let arr: Vec<i32> = config.arr;
    let warmup = config.warmup;
    let target = config.target;

    println!("Warmup: {}", warmup);
    println!("Jumlah Data: {}", arr.len());
    println!("Target: {}", target);

    let mut sorted_arr = arr.clone();
    sorted_arr.sort();

    for _ in 0..warmup {
        helper::linear_search(&arr, target);
        helper::binary_search(&sorted_arr, target);
    }

    println!("\nLinear Search");
    let start_linear = Instant::now();

    let result_linear = helper::linear_search(&arr, target);

    let duration_linear = start_linear.elapsed().as_nanos();

    match result_linear {
        Some(index) => println!("Index: {} | Time: {:?} ns", index, duration_linear),
        None => println!("Element not found"),
    }

    println!("Binary Search");
    let start_binary = Instant::now();

    let result_binary = helper::binary_search(&sorted_arr, target);

    let duration_binary = start_binary.elapsed().as_nanos();

    match result_binary {
        Some(index) => println!("Index: {} | Time: {:?} ns", index, duration_binary),
        None => println!("Element not found"),
    }
    println!();
}
