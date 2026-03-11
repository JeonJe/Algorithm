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
    static int[][] arr;
    static boolean[] visited;

    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, 1, 0, -1};

    static int r, c, k;
    static int count;

    public static void main(String[] args) throws Exception {
        arr = new int[4][2];

        for (int i = 0; i < 4; i++) {
            st = new StringTokenizer(br.readLine());
            arr[i][0] = Integer.parseInt(st.nextToken());
            arr[i][1] = Integer.parseInt(st.nextToken());
        }

        visited = new boolean[4];


        int answer = Integer.MAX_VALUE;

        for (int i = 1; i < 4; i++) {
            for (int j = 1; j < 4; j++) {
                for (int k = 1; k < 4; k++) {
                    if (i != j && j != k && k != i) {
                        int sum = (int) (distance(0, i) + distance(i, j) + distance(j, k));
                        answer = Math.min(answer, sum);
                    }

                }
            }
        }

        System.out.println(answer);


    }

    private static double distance(int i, int j) {
        return Math.sqrt(Math.pow(arr[i][0] - arr[j][0], 2) + Math.pow(arr[i][1] - arr[j][1], 2));
    }

}