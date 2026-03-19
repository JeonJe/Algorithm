import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    public static final int INT = 1_000_000;
    public static final int LIMIT_COUNT = INT;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;

    static final int INF = Integer.MAX_VALUE;
    static final long LINF = Long.MAX_VALUE;
    static int n;
    static boolean[] visited;

    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, 1, 0, -1};

    static int r, c, k;
    static int count;

    //숫자를 1개씩 써서 만들 수 있는 숫자 모음
    private static List<Long> list = new ArrayList<>();

    public static void main(String[] args) throws Exception {

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int max = 0;
        for (int i = 0; i < n - 2; i++) {
            for (int j = i + 1; j < n - 1; j++) {
                for (int k = j + 1; k < n; k++) {
                    if (arr[i] + arr[j] + arr[k] <= m) {
                        max = Math.max(max, arr[i] + arr[j] + arr[k]);
                    }
                }
            }
        }

        System.out.println(max);

    }


}