import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;
    static int[][] r;
    static int[][] m;
    static int n = 0, k = 0;

    public static void main(String[] args) throws Exception {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        int[] a = new int[n];
        String[] cans = br.readLine().split(" ");
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(cans[i]);
        }
        r = new int[k][n];
        m = new int[k][n];

        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                r[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                m[i][j] = Integer.parseInt(st.nextToken());
            }
        }


        int result = dfs(0, a);
        System.out.println(result);


    }

    private static int dfs(int day, int[] a) {
        if (day == k) {
            return 0;
        }

        int best = 0;
        //랑이
        for (int i = 0; i < n; i++) {
            if (a[i] == 0) {
                continue;
            }
            a[i]--;
            //메리
            for (int j = 0; j < n; j++) {
                if (a[j] == 0) {
                    continue;
                }
                a[j]--;
                best = Math.max(best, r[day][i] + m[day][j] + dfs(day + 1, a));
                a[j]++;
            }
            a[i]++;
        }
        return best;

    }

}