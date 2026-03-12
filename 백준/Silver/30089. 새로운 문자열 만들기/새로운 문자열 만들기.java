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

        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            String s = br.readLine();
            String reverse = new StringBuilder(s).reverse().toString();

            int maxLength = 0;

            //0 부터 length까지 정방향 postfix랑,  역방향 prefix 를 짤라서 같다면 그때 length 추가
            for (int j = 1; j <= s.length(); j++) {
                String a = s.substring(s.length() - j);
                String b = reverse.substring(0, j);
                if (a.equals(b)) {
                    maxLength = Math.max(maxLength, a.length());
                }
            }

            System.out.println(new StringBuilder(s).append(reverse.substring(maxLength)));

        }
    }
}