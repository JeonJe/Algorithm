import java.util.*;
import java.io.*;

public class BOJ_10026 {
  static int[] dx = { 1, 0, -1, 0 };
  static int[] dy = { 0, 1, 0, -1 };
  static int N;
  static char[][] board;
  static int answer1, answer2;
  
  static class Pair {
    int x, y;

    public Pair(int x, int y) {
      this.x = x;
      this.y = y;
    }
  }

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    N = Integer.parseInt(br.readLine());

    board = new char[N][N];

    for (int i = 0; i < N; i++) {
      board[i] = br.readLine().toCharArray();
    }

    // 적록색약이 없는 사람 bfs
    answer1 = find_area(board);

    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        if(board[i][j] == 'R') {
          board[i][j] = 'G';
        }
      }
    }
    // 적록색이 있는 사람 bfs
    answer2 = find_area(board);
    System.out.println(answer1 +" "+ answer2);
  }

  static int find_area(char[][] board) {
    boolean[][] visited = new boolean[N][N];
    int cnt = 0;
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        if (!visited[i][j]) {
          visited[i][j] = true;
          cnt++;
          bfs(board, visited, i, j);
        }
      }
    }
    return cnt;
  }

  static void bfs(char[][] board, boolean[][] visited, int x, int y) {

    char initColor = board[x][y];

    Queue<Pair> queue = new LinkedList<>();
    queue.offer(new Pair(x, y));

    while (!queue.isEmpty()) {
      Pair current = queue.poll();
      int cx = current.x;
      int cy = current.y;

      for (int i = 0; i < 4; i++) {
        int nx = cx + dx[i];
        int ny = cy + dy[i];

        if (0 <= nx && nx < N && 0 <= ny && ny < N) {
          if (!visited[nx][ny] && board[nx][ny] == initColor) {
            visited[nx][ny] = true;
            queue.offer(new Pair(nx, ny));
          }
        }
      }
    }
    return;
  }
}
