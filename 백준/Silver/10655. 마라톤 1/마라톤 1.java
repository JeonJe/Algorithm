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
    static int[][] arr;
    static int total;
    static int[][] dp;

    public static void main(String[] args) throws Exception {

        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        arr = new int[n][2];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            arr[i][0] = Integer.parseInt(st.nextToken());
            arr[i][1] = Integer.parseInt(st.nextToken());
        }

        int sum = 0;
        int answer = Integer.MAX_VALUE;
        for (int i = 1; i < n; i++) {
            sum += distance(i, i - 1);
        }

        for (int i = 1; i < n - 1; i++) {
            // i가 빠졌을 때 없어지는 거리
            int deleted = distance(i - 1, i) + distance(i, i + 1);
            int added = distance(i - 1, i + 1);
            int saving = deleted - added;
            answer = Math.min(answer, sum - saving);
        }

        System.out.println(answer);
        br.readLine();
    }

    private static int distance(int index1, int index2) {
        return Math.abs(arr[index1][0] - arr[index2][0]) + Math.abs(arr[index1][1] - arr[index2][1]);
    }
}