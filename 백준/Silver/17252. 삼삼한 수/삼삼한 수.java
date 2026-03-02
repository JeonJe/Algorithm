import java.io.BufferedReader;
import java.io.InputStreamReader;
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

        n = Integer.parseInt(br.readLine());
        if(n == 0) {
            System.out.println("NO");
            return;
        }

        dfs(0, 0);

        System.out.println("NO");

    }

    private static void dfs(int idx, int sum) {
        if (sum > n || idx > 20) {
            return;
        }
        if (sum == n) {
            System.out.println("YES");
            System.exit(0);
        }


        dfs(idx + 1, sum + (int) Math.pow(3, idx));
        dfs(idx + 1, sum);


    }
}