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

        int[] arr = new int[5];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 5; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }


        for (int i = 1; i < 999_999; i++) {
            int count = 0;
            for (int j = 0; j < 5; j++) {
                //i가 arr[i] 의 배수
                if (i % arr[j] == 0) {
                    count++;
                }
            }

            if (count >= 3) {
                System.out.println(i);
                return;
            }
        }


        br.readLine();


    }
}