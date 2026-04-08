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
            int amount = Integer.parseInt(br.readLine());
            int[][] arr = new int[amount][2];

            for (int j = 0; j < amount; j++) {
                st = new StringTokenizer(br.readLine());
                arr[j][0] = Integer.parseInt(st.nextToken());
                arr[j][1] = Integer.parseInt(st.nextToken());
            }

            //같은 가격으로 최대한 많은 중량을 살 수 있는 맛살
            int goodIdx = 0;
            double min = Double.MAX_VALUE;
            for( int j = 0; j < amount; j++) {
                double cur = (double) arr[j][1] / arr[j][0];

                //1g에 가격이 제일싸냐?
                if(cur < min) {
                    goodIdx = j;
                    min = cur;
                } else if(cur == min && arr[j][1] < arr[goodIdx][1]) {
                    goodIdx = j;
                }
            }

            System.out.println(arr[goodIdx][1]);

        }



    }
}