import java.util.*;

public class Main {

  static int n;
  static int[] dx = {0, 1, 0, -1};
  static int[] dy = {1, 0, -1, 0};
  static int[][] board;

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    n = sc.nextInt();
    board = new int[n][n];

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        board[i][j] = sc.nextInt();
      }
    }
    int cnt = 0;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        if (isSatisfied(i, j)) {
          cnt++;
        }
      }
    }

    System.out.println(cnt);
  }

  static boolean isSatisfied(int x, int y) {
    int cnt = 0;
    for (int i = 0; i < 4; i++) {
      int nx = x + dx[i];
      int ny = y + dy[i];

      if (0 <= nx && nx < n && 0 <= ny && ny < n) {
        if (board[nx][ny] == 1) {
          cnt++;
        }
      }
    }
    return cnt >= 3;
  }


}
