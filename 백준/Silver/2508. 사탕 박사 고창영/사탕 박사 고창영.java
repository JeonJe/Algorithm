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
    static int[] arr;
    static int total;
    static int[][] dp;

    public static void main(String[] args) throws Exception {
        int t = Integer.parseInt(br.readLine());


        for (int i = 0; i < t; i++) {
            int count = 0;

            br.readLine();

            StringTokenizer st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            char[][] map = new char[r][c];
            boolean[][] visited = new boolean[r][c];

            for (int x = 0; x < r; x++) {
                map[x] = br.readLine().toCharArray();
            }

            for (int x = 0; x < r; x++) {
                for (int y = 0; y < c; y++) {
                    if (visited[x][y]) {
                        continue;
                    }

                    visited[x][y] = true;
                    //가로 사탕 확인
                    if (map[x][y] == '>') {
                        if (y + 1 < c && map[x][y + 1] == 'o' && y + 2 < c && map[x][y + 2] == '<') {
                            count++;
                            visited[x][y + 1] = true;
                            visited[x][y + 2] = true;
                        }
                    }
                    //세로 사탕 확인
                    if (map[x][y] == 'v') {
                        if (x + 1 < r && map[x + 1][y] == 'o' && x + 2 < r && map[x + 2][y] == '^') {
                            count++;
                            visited[x + 1][y] = true;
                            visited[x + 2][y] = true;
                        }
                    }
                }
            }
            System.out.println(count);
        }


        br.readLine();


    }
}