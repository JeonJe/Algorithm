import java.io.*;
import java.util.*;

public class Main {
  static Boolean isPossible = false;
  static int[] dx = {1,0};
  static int[] dy = {0,1};
  public static void main(String[] args) throws Exception {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(rd.readLine());
    int[][] board = new int[N][N];
    boolean[][] visited = new boolean[N][N];
    StringTokenizer st;
    for (int i = 0; i < N; i++) {
      st = new StringTokenizer(rd.readLine());
      for (int j = 0; j < N; j++) {
        board[i][j] = Integer.parseInt(st.nextToken());
      }
    }
    visited[0][0] = true;
    dfs(0,0, board, visited);
    if (isPossible) {
      System.out.println("HaruHaru");
    } else {
      System.out.println("Hing");
    }
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
