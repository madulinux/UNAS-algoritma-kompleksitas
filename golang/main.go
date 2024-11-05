package main

import (
	"encoding/json"
	"fmt"
	"io"
	"os"
	"sort"
	"time"
)

func runSearch(searchType string, arr []int, target int, warmup int) {
	if searchType != "linear" && searchType != "binary" {
		fmt.Println("Invalid search type. Please use 'linear' or 'binary'.")
		return
	}

	if searchType == "binary" {
		// fmt.Println("Sorting array for binary search")
		sort.Ints(arr)
	}

	// warmup
	for i := 0; i < warmup; i++ {
		if searchType == "linear" {
			linearSearch(arr, target)
		} else {
			binarySearch(arr, target)
		}
	}

	// Measure time before execution
	start := time.Now()
	var result int
	if searchType == "linear" {
		result = linearSearch(arr, target)
	} else {
		result = binarySearch(arr, target)
	}
	// Measure time after execution
	duration := time.Since(start)
	fmt.Printf("Index: %d | Time: %d ns\n", result, duration.Nanoseconds())
}

type Config struct {
	Target int   `json:"target"`
	Arr    []int `json:"arr"`
	Warmup int   `json:"warmup"`
}

func getConfig() (target int, arr []int, warmup int) {
	jsonFile, err := os.Open("../config.json")
	if err != nil {
		fmt.Println("Error opening JSON file:", err)
		return
	}
	defer jsonFile.Close()

	byteValue, _ := io.ReadAll(jsonFile)

	var config Config
	json.Unmarshal(byteValue, &config)

	return config.Target, config.Arr, config.Warmup
}

func main() {
	// read json file
	target, arr, warmup := getConfig()

	fmt.Println("Warmup: ", warmup)
	fmt.Println("Jumlah Data: ", len(arr))
	fmt.Println("Target:", target)
	fmt.Println()

	fmt.Println("Linear Search")
	runSearch("linear", arr, target, warmup)
	fmt.Println("Binary Search")
	runSearch("binary", arr, target, warmup)
	fmt.Println()
}
