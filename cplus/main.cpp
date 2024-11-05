#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <chrono>
// #include <nlohmann/json.hpp> // Include the JSON library
#include "include/json.hpp"


using json = nlohmann::json;

struct Config {
    int target;
    std::vector<int> arr;
    int warmup;
};

int linearSearch(const std::vector<int>& arr, int target);
int binarySearch(const std::vector<int>& arr, int target);
Config getConfig();

void runSearch(const std::string& searchType, std::vector<int> arr, int target, int warmup) {
    if (searchType != "linear" && searchType != "binary") {
        std::cout << "Invalid search type. Please use 'linear' or 'binary'." << std::endl;
        return;
    }

    if (searchType == "binary") {
        std::sort(arr.begin(), arr.end());
    }

    for (int i = 0; i < warmup; ++i) {
        if (searchType == "linear") {
            linearSearch(arr, target);
        } else {
            binarySearch(arr, target);
        }
    }

    auto start = std::chrono::high_resolution_clock::now();

    int result;
    if (searchType == "linear") {
        result = linearSearch(arr, target);
    } else {
        result = binarySearch(arr, target);
    }

    auto duration = std::chrono::high_resolution_clock::now() - start;
    auto duration_ns = std::chrono::duration_cast<std::chrono::nanoseconds>(duration).count();

    std::cout << "Index: " << result << " | Time: " << duration_ns << " ns" << std::endl;
}

int main() {
    Config config = getConfig();

    std::cout << "Warmup: " << config.warmup << std::endl;
    std::cout << "Jumlah Data: " << config.arr.size() << std::endl;
    std::cout << "Target: " << config.target << std::endl;
    std::cout << std::endl;

    std::cout << "Linear Search" << std::endl;
    runSearch("linear", config.arr, config.target, config.warmup);
    std::cout << "Binary Search" << std::endl;
    runSearch("binary", config.arr, config.target, config.warmup);
    std::cout << std::endl;

    return 0;
}

Config getConfig() {
    std::ifstream jsonFile("../config.json");
    if (!jsonFile.is_open()) {
        std::cerr << "Error opening JSON file" << std::endl;
        exit(EXIT_FAILURE);
    }

    json j;
    jsonFile >> j;

    Config config;
    config.target = j["target"];
    config.arr = j["arr"].get<std::vector<int>>();
    config.warmup = j["warmup"];

    return config;
}