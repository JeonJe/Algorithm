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
    static int[][] arr;
    static boolean[] visited;

    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, 1, 0, -1};

    static int r, c, k;
    static int count;

    public static void main(String[] args) throws Exception {

        while (true) {
            String input = br.readLine();
            if (input.equals("#")) {
                break;
            }

            StringBuilder sb = new StringBuilder();
            for (int i = input.length() - 1; i >= 0; i--) {
                char ch = input.charAt(i);
                if (ch == 'b') {
                    sb.append('d');
                } else if (ch == 'd') {
                    sb.append('b');
                } else if (ch == 'p') {
                    sb.append('q');
                } else if (ch == 'q') {
                    sb.append('p');
                } else if (ch == 'i' || ch == 'o' || ch == 'v' || ch == 'w' || ch == 'x') {
                    sb.append(ch);
                } else {
                    sb = new StringBuilder("INVALID");
                    break;
                }
            }
            System.out.println(sb.toString());

        }

    }
}