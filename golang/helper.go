package main

import (
	"fmt"
	"math/rand"
	"strings"
	"time"
)

func linearSearch(arr []int, target int) int {
	for i, v := range arr {
		if v == target {
			return i
		}
	}
	return -1
}

func binarySearch(arr []int, target int) int {
	low, high := 0, len(arr)-1
	for low <= high {
		mid := low + (high-low)/2
		if arr[mid] == target {
			return mid
		}
		if arr[mid] < target {
			low = mid + 1
		} else {
			high = mid - 1
		}
	}
	return -1
}

func GenerateRandomArray(size int, maxValue int) []int {
	rand.New(rand.NewSource(time.Now().UnixNano()))
	arr := make([]int, size)
	for i := range arr {
		arr[i] = rand.Intn(maxValue) // Generate a random integer between 0 and maxValue-1
	}
	return arr
}

func GenerateRandomPermutation(n int) []int {
	// Create a slice with numbers from 1 to n
	arr := make([]int, n)
	for i := 0; i < n; i++ {
		arr[i] = i + 1
	}

	// Seed the random number generator
	rand.Seed(time.Now().UnixNano())

	// Shuffle the slice
	rand.Shuffle(n, func(i, j int) {
		arr[i], arr[j] = arr[j], arr[i]
	})

	return arr
}
func FormatNumberWithThousandSeparator(n int) string {
	in := fmt.Sprintf("%d", n)
	out := make([]string, 0, len(in)+(len(in)-1)/3)
	for i, v := range in {
		if i > 0 && (len(in)-i)%3 == 0 {
			out = append(out, ".")
		}
		out = append(out, string(v))
	}
	return strings.Join(out, "")
}
