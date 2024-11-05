import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.List;
import java.text.NumberFormat;
import java.util.Locale;
import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

public class Main {
    public static void main(String[] args) {
        Config config = readJsonFile("../config.json");
        if (config == null) {
            System.out.println("Error reading JSON file.");
            return;
        }

        List<Integer> arr = config.arr;
        int target = config.target;
        int warmup = config.warmup;

        System.out.println("Warmup: " + warmup);
        System.out.println("Jumlah Data: " + arr.size());
        System.out.println("Target: " + target);
        System.out.println();

        System.out.println("Linear Search");
        runSearch("linear", arr, target, warmup);
        System.out.println("Binary Search");
        runSearch("binary", arr, target, warmup);
        System.out.println();
    }

    private static Config readJsonFile(String filePath) {
        try (FileReader reader = new FileReader(filePath)) {
            return new Gson().fromJson(reader, Config.class);
        } catch (IOException e) {
            System.out.println("Error opening JSON file: " + e.getMessage());
            return null;
        }
    }

    private static void runSearch(String searchType, List<Integer> arr, int target, int warmup) {
        if (!searchType.equals("linear") && !searchType.equals("binary")) {
            System.out.println("Invalid search type. Please use 'linear' or 'binary'.");
            return;
        }

        if (searchType.equals("binary")) {
            // System.out.println("Sorting array for binary search");
            arr.sort(Integer::compareTo);
        }

        // Fase pemanasan
        for (int i = 0; i < warmup; i++) {
            if (searchType.equals("linear")) {
                Helper.linearSearch(arr, target);
            } else {
                Helper.binarySearch(arr, target);
            }
        }

        // Measure memory usage before execution
        // Runtime runtime = Runtime.getRuntime();
        // long memStart = runtime.totalMemory() - runtime.freeMemory();

        // Measure time before execution
        long startTime = System.nanoTime();

        int result;
        if (searchType.equals("linear")) {
            result = Helper.linearSearch(arr, target);
        } else {
            result = Helper.binarySearch(arr, target);
        }

        // Measure time after execution
        long duration = System.nanoTime() - startTime;
        System.out.printf("Index: %d | Time: %d ns\n", result, duration);
    }

    private static class Config {
        int target;
        List<Integer> arr;
        int warmup;
    }
}