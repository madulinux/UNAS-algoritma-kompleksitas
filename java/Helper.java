import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;

public class Helper {

    public static int linearSearch(List<Integer> arr, int target) {
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) == target) {
                return i;
            }
        }
        return -1;
    }

    public static int binarySearch(List<Integer> arr, int target) {
        int low = 0, high = arr.size() - 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (arr.get(mid) == target) {
                return mid;
            }
            if (arr.get(mid) < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return -1;
    }

    public static List<Integer> generateRandomArray(int size, int maxValue) {
        Random rand = new Random();
        List<Integer> arr = new ArrayList<>(size);
        for (int i = 0; i < size; i++) {
            arr.add(rand.nextInt(maxValue)); // Generate a random integer between 0 and maxValue-1
        }
        return arr;
    }

    public static List<Integer> generateRandomPermutation(int n) {
        List<Integer> arr = new ArrayList<>(n);
        for (int i = 0; i < n; i++) {
            arr.add(i + 1);
        }

        Collections.shuffle(arr, new Random());
        return arr;
    }
}