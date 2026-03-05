import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;

    static final int INF = Integer.MAX_VALUE;
    static final long LINF = Long.MAX_VALUE;
    static int n;
    static int[] arr;
    static int total;
    static int[][] dp;

    public static void main(String[] args) throws Exception {
        int n = Integer.parseInt(br.readLine());

        arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        int count = 0;
        while (true) {

            int max = arr[0];
            int maxIndex = 0;

            for (int i = 1; i < n; i++) {
                if (arr[i] >= max) {
                    max = arr[i];
                    maxIndex = i;
                }
            }

            if (max >= arr[0] && maxIndex != 0) {
                arr[maxIndex]--;
                arr[0]++;
                count++;
            } else {
                break;
            }
        }

        System.out.println(count);
        br.readLine();


    }
}