const fs = require('fs');
const { linearSearch, binarySearch } = require('./helper');

function runSearch(searchType, arr, target, warmup) {
    if (searchType !== 'linear' && searchType !== 'binary') {
        console.log("Invalid search type. Please use 'linear' or 'binary'.");
        return [-1, 0, 0];
    }

    if (searchType === 'binary') {
        // console.log("Sorting array for binary search");
        arr.sort((a, b) => a - b);
    }

    for (let i = 0; i < warmup; i++) {
        if (searchType === 'linear') {
            linearSearch(arr, target);
        } else {
            binarySearch(arr, target);
        }
    }

    // Measure memory usage before execution
    // const memStart = process.memoryUsage().heapUsed;

    // Measure time before execution
    const start = process.hrtime.bigint();

    let result;
    if (searchType === 'linear') {
        result = linearSearch(arr, target);
    } else {
        result = binarySearch(arr, target);
    }

    // Measure time after execution
    const end = process.hrtime.bigint();
    const duration = end - start; // Duration in nanoseconds

    // Measure memory usage after execution
    // const memEnd = process.memoryUsage().heapUsed;

    return [result, duration];
}

function main() {
    // Read JSON file
    fs.readFile('../config.json', 'utf8', (err, data) => {
        if (err) {
            console.log("Error opening JSON file:", err);
            return;
        }

        const config = JSON.parse(data);
        const arr = config.arr;
        const target = config.target;
        const warmup = config.warmup;
        let formattedDuration = 0;

        console.log("Warmup: ", warmup);
        console.log("Jumlah Data: ", arr.length);
        console.log("Target: ", target);
        console.log();
        console.log("Linear Search");
        let [result, duration] = runSearch('linear', arr, target, warmup);

        // if (result !== -1) {
        //     console.log(`Element found at index ${result}`);
        // } else {
        //     console.log("Element not found");
        // }
        // formattedDuration = duration.toLocaleString('id-ID');
        console.log(`Index: ${result} | Time: ${duration} ns`);
        // console.log(`Time taken: ${duration} ns`);
        // console.log(`Memory used: ${memUsed} bytes`);
        console.log("Binary Search");
        [result, duration] = runSearch('binary', arr, target, warmup);

        // if (result !== -1) {
        //     console.log(`Element found at index ${result}`);
        // } else {
        //     console.log("Element not found");
        // }
        // formattedDuration = duration.toLocaleString('id-ID');
        console.log(`Index: ${result} | Time: ${duration} ns`);
        console.log();
    });
}

main();