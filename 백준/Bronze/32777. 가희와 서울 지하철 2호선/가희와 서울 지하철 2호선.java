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

        int q = Integer.parseInt(br.readLine());


        for (int i = 0; i < q; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());

            int inner = (end - start + 43) % 43;
            int outer = (start - end + 43) % 43;

            if (inner < outer) sb.append("Inner circle line\n");
            else if (outer < inner) sb.append("Outer circle line\n");
            else sb.append("Same\n");
        }

        System.out.print(sb);
    }


}