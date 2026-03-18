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
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());

        //x - a명씩 들어가는 방의 갯수  (최소 a명이 1일떄 방 300개)
        //y - b명씩 들어가는 방의 갯수
        //z - c명씩 들어가는 방의 갯수
        for (int x = 0; x <= 300; x++) {
            for (int y = 0; y <= 300; y++) {
                for (int z = 0; z <= 300; z++) {
                    if (a * x + b * y + c * z == n) {
                        System.out.println("1");
                        return;
                    }
                    if (a * x + b * y + c * z > n) {
                        break;
                    }
                }
            }
        }
        System.out.println("0");
    }


}