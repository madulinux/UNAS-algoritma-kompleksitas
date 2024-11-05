<?php

include 'helper.php';

function runSearch($searchType, $arr, $target, $warmup) {
    if ($searchType !== "linear" && $searchType !== "binary") {
        echo "Invalid search type. Please use 'linear' or 'binary'.\n";
        return [-1, 0, 0];
    }

    if ($searchType === "binary") {
        // echo "Sorting array for binary search\n";
        sort($arr);
    }

    for ($i = 0; $i < $warmup; $i++) {
        if ($searchType === "linear") {
            linearSearch($arr, $target);
        } else {
            binarySearch($arr, $target);
        }
    }

    // Measure memory usage before execution
    // $memStart = memory_get_usage();

    // Measure time before execution
    $start = hrtime(true); // Start time in nanoseconds

    if ($searchType === "linear") {
        $result = linearSearch($arr, $target);
    } else {
        $result = binarySearch($arr, $target);
    }

    // Measure time after execution
    $duration = hrtime(true) - $start; // Duration in nanoseconds

    // Measure memory usage after execution
    // $memEnd = memory_get_usage();
    // if ($result !== -1) {
    //     echo "Element found at index $result\n";
    // } else {
    //     echo "Element not found\n";
    // }
    // $formattedDuration = number_format($duration, 0, ',', '.');
    echo "Index: $result | Time: $duration ns";
}

function main() {
    // Read JSON file
    $jsonString = file_get_contents('../config.json');
    if ($jsonString === false) {
        echo "Error opening JSON file.\n";
        return;
    }

    $config = json_decode($jsonString, true);
    if ($config === null) {
        echo "Error decoding JSON.\n";
        return;
    }

    $arr = $config['arr'];
    $target = $config['target'];
    $warmup = $config['warmup'];
    
    echo "Warmup: $warmup\n";
    echo "Jumlah Data: " . count($arr) . "\n";
    echo "Target: $target\n\n";

    echo "Linear Search\n";
    runSearch("linear", $arr, $target, $warmup);
    echo PHP_EOL;

    echo "Binary Search\n";
    runSearch("binary", $arr, $target, $warmup);
    echo PHP_EOL;
    echo PHP_EOL;
}

main();
?>