import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;

    public static void main(String[] args) throws Exception {
        int testCase = Integer.parseInt(br.readLine());

        for (int t = 1; t <= testCase; t++) {
            startGame();
        }
    }

    private static void startGame() throws IOException {
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];

        String[] numbers = br.readLine().split(" ");
        int oddCount = 0;
        int evenCount = 0;
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(numbers[i]);
            if (arr[i] % 2 != 0) {
                oddCount++;
            } else {
                evenCount++;
            }
        }

        if (oddCount == evenCount) {
            System.out.println("heeda0528");
        } else {
            if (Math.max(oddCount, evenCount) % 2 == 0) {
                System.out.println("heeda0528");
            } else {
                System.out.println("amsminn");
            }
        }
    }

}