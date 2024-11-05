<?php

function linearSearch($arr, $target) {
    foreach ($arr as $i => $v) {
        if ($v === $target) {
            return $i;
        }
    }
    return -1;
}

function binarySearch($arr, $target) {
    $low = 0;
    $high = count($arr) - 1;
    while ($low <= $high) {
        $mid = $low + (int)(($high - $low) / 2);
        if ($arr[$mid] === $target) {
            return $mid;
        }
        if ($arr[$mid] < $target) {
            $low = $mid + 1;
        } else {
            $high = $mid - 1;
        }
    }
    return -1;
}

function generateRandomArray($size, $maxValue) {
    $arr = [];
    for ($i = 0; $i < $size; $i++) {
        $arr[] = rand(0, $maxValue - 1);
    }
    return $arr;
}

function generateRandomPermutation($n) {
    $arr = range(1, $n);
    shuffle($arr);
    return $arr;
}

?>