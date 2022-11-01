import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int n;
    static int[][] map;
    static boolean[][] visited;
    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, -1, 0, 1};


    static void bfs(int i, int j, int k) {

        Queue<Point> queue = new LinkedList<Point>();
        queue.add(new Point(i, j));

        while (!queue.isEmpty()) {
            Point p = queue.poll();

            for (int r = 0; r < 4; r++) {
                int nx = p.x + dx[r];
                int ny = p.y + dy[r];

                if (0 <= nx && nx < n && 0 <= ny && ny < n) {
                    if (map[nx][ny] > k && !visited[nx][ny]) {
                        visited[nx][ny] = true;
                        queue.add(new Point(nx, ny));


                    }
                }
            }
        }
        return;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        map = new int[n][n];

        int maxHeight = 0;

//         맥스값 추출
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                if (map[i][j] > maxHeight) {
                    maxHeight = map[i][j];
                }
            }
        }
        int max = 0;
        for (int k = 0; k < maxHeight + 1; k++) {
            visited = new boolean[n][n];

            for (boolean[] row : visited) {
                Arrays.fill(row, false);
            }

            int cnt = 0;

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (!visited[i][j] && map[i][j] > k) {
                        bfs(i, j, k);
                        cnt += 1;
                    }
                }
            }
            max = Math.max(max, cnt);
        }
        System.out.println(max);

    }
}

