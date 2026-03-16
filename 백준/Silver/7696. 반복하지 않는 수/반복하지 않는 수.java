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

        StringBuilder sb = new StringBuilder();

        visited = new boolean[10];

        // 1부터 1_000_000 번까지 반복하지 않는 수를 만듬
        int[] arr = new int[LIMIT_COUNT + 1];

        int cur = 1;
        int idx = 1;
        while(idx <= 1_000_000) {
            if (!isRepeat(cur)) {
                arr[idx] = cur;
                idx++;
            }
            cur++;
        }

        while (true) {
            String input = br.readLine();
            if (input.equals("0")) {
                break;
            }
            int targetIndex = Integer.parseInt(input);
            sb.append(arr[targetIndex]).append("\n");
        }
        System.out.println(sb);

    }

    private static boolean isRepeat(int num) {
        for(int i = 0 ; i < 10; i++) {
            visited[i] = false;
        }

        while (num > 0) {
            int digit = num % 10;
            if(visited[digit]) {
                return true;
            }
            visited[digit] = true;
            num /= 10;
        }
        return false;
    }


}