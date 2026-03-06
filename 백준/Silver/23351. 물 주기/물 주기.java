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

        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        // A개 씩 나눈 화문 그룹 갯수
        int groupCount = n / a;

        //수분량
        int x = k;
        int day = 0;

        while (x >= groupCount) {
            day += groupCount;
            // 각 그룹의 감소량, 그룹씩 돌아가면서 주고, b만큼 물을 줌
            x -= groupCount - b;
        }

        // 마지막 바퀴의 x일쨰 죽음
        day += x;

        System.out.println(day);
        br.readLine();
    }
}