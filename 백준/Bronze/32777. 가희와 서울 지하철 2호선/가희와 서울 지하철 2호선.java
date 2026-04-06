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

            if(start == end) {
                System.out.println("Same");
                continue;
            }

            int rightDirection;
            int leftDirection;

            if (start <= end) {
                rightDirection = end - start;
                leftDirection = 43 - end + start;
            } else {
                rightDirection = 43 - start + end;
                leftDirection = start - end;
            }

            if (leftDirection < rightDirection) {
                System.out.println("Outer circle line");
            } else if (leftDirection > rightDirection) {
                System.out.println("Inner circle line");
            }
        }


    }


}