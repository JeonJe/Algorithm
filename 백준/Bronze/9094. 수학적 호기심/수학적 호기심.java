import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;
    static int n = 0, m = 0;
    static boolean[] visited;

    public static void main(String[] args) throws Exception {
        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());

            int count = 0;
            for (int a = 1; a < n; a++) {
                for (int b = a + 1; b < n; b++) {

                    // 정수 쌍 (a,b) 중에서 (a^2 + b^ 2 +m ) / (a*b) 가 정수
                    if (Math.floor((double) (a * a + b * b + m) / (a * b)) == (double) (a * a + b * b + m) / (a * b)) {
                        count++;
                    }
                }
            }
            System.out.println(count);
        }

    }
}