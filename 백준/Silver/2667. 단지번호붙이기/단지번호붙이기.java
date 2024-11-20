
import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

class Main {

    static int n;
    static int[][] graph;
    static boolean[][] visited;
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, -1, 0, 1};
    static int count = 0;
    static List<Integer> numbers = new ArrayList<>();
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(reader.readLine());
        graph = new int[n][n];
        visited = new boolean[n][n];

        for (int i = 0; i < n; i++) {
            String row = reader.readLine();
            for (int j = 0; j < row.length(); j++) {
                graph[i][j] = Character.getNumericValue(row.charAt(j));
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (graph[i][j] == 1 && !visited[i][j]) {
                    count++;
                    bfs(i, j);
                }
            }
        }
        sb.append(count).append("\n");
        numbers.stream()
                .sorted()
                .forEach(num -> sb.append(num).append("\n"));

        System.out.println(sb.toString());

    }

    private static void bfs(int row, int col) {
        visited[row][col] = true;
        Deque<Point> queue = new ArrayDeque<>();
        queue.offer(new Point(row, col));
        int houseCount = 1;

        while (!queue.isEmpty()) {

            Point currentPoint = queue.poll();
            for (int i = 0; i < 4; i++) {
                int nx = currentPoint.x + dx[i];
                int ny = currentPoint.y + dy[i];

                if (nx < 0 || nx >= n || ny < 0 || ny >= n) {
                    continue;
                }

                if (graph[nx][ny] == 1 && !visited[nx][ny]) {
                    queue.offer(new Point(nx, ny));
                    visited[nx][ny] = true;
                    houseCount++;
                }
            }
        }
        numbers.add(houseCount);
    }
}


