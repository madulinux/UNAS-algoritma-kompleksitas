#include <vector>
#include <random>
#include <string>
#include <sstream>
#include <iomanip>
#include <algorithm>

int linearSearch(const std::vector<int>& arr, int target) {
    for (size_t i = 0; i < arr.size(); ++i) {
        if (arr[i] == target) {
            return i;
        }
    }
    return -1;
}

int binarySearch(const std::vector<int>& arr, int target) {
    int low = 0, high = arr.size() - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == target) {
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

std::vector<int> generateRandomArray(int size, int maxValue) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(0, maxValue - 1);

    std::vector<int> arr(size);
    for (int& val : arr) {
        val = dis(gen);
    }
    return arr;
}

std::vector<int> generateRandomPermutation(int n) {
    std::vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        arr[i] = i + 1;
    }

    std::random_device rd;
    std::mt19937 gen(rd());
    std::shuffle(arr.begin(), arr.end(), gen);

    return arr;
}

std::string formatNumberWithThousandSeparator(int n) {
    std::stringstream ss;
    ss.imbue(std::locale(""));
    ss << std::fixed << n;
    return ss.str();
}