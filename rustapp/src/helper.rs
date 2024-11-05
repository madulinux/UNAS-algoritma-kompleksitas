pub fn linear_search(arr: &[i32], target: i32) -> Option<usize> {
    for (i, &value) in arr.iter().enumerate() {
        if value == target {
            return Some(i);
        }
    }
    None
}

pub fn binary_search(arr: &[i32], target: i32) -> Option<usize> {
    let mut low = 0;
    let mut high = arr.len() as isize - 1;

    while low <= high {
        let mid = low + (high - low) / 2;
        let mid_value = arr[mid as usize];

        if mid_value == target {
            return Some(mid as usize);
        } else if mid_value < target {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    None
}
