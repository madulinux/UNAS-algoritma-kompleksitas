function linearSearch(arr, target) {
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === target) {
            return i;
        }
    }
    return -1;
}

function binarySearch(arr, target) {
    let low = 0, high = arr.length - 1;
    while (low <= high) {
        const mid = Math.floor(low + (high - low) / 2);
        if (arr[mid] === target) {
            return mid;
        }
        if (arr[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return -1;
}

function generateRandomArray(size, maxValue) {
    const arr = new Array(size);
    for (let i = 0; i < size; i++) {
        arr[i] = Math.floor(Math.random() * maxValue); // Generate a random integer between 0 and maxValue-1
    }
    return arr;
}

function generateRandomPermutation(n) {
    const arr = Array.from({ length: n }, (_, i) => i + 1);

    // Shuffle the array
    for (let i = n - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [arr[i], arr[j]] = [arr[j], arr[i]];
    }

    return arr;
}

module.exports = {
    linearSearch,
    binarySearch,
    generateRandomArray,
    generateRandomPermutation
};