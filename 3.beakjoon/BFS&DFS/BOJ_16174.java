import java.io.*;
import java.util.*;

public class BOJ_16174 {
  static Boolean isPossible = false;
  static int[] dx = {1,0};
  static int[] dy = {0,1};
  public static void main(String[] args) throws Exception {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter w = new BufferedWriter(new OutputStreamWriter(System.out));

    int N = Integer.parseInt(rd.readLine());
    int[][] board = new int[N][N];
    boolean[][] visited = new boolean[N][N];
    for (int i = 0; i < N; i++) {
      board[i] = Arrays.stream(rd.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
    }

    visited[0][0] = true;
    dfs(0,0, board, visited);
    if (isPossible) {
      w.write("HaruHaru");
    } else {
      w.write("Hing");
    }
    w.flush();
    w.close();
    rd.close();
  }

  static void dfs(int x, int y, int[][] board, boolean[][] visited){
    int boardLength = board.length;
    if (x == boardLength-1 && y == boardLength-1) {
      isPossible = true;
      return;
    }
    int jumpDistance = board[x][y];
    for (int i = 0; i < 2; i++) {
      int nx = x + dx[i] * jumpDistance;
      int ny = y + dy[i] * jumpDistance;
      if (0 <= nx && nx < boardLength && 0 <= ny && ny < boardLength && !visited[nx][ny]) {
        visited[nx][ny] = true;
        dfs(nx, ny, board, visited);
      }
    }
    return ;
  }
}
