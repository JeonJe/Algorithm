import java.util.Scanner;

public class Main {

  static int[][] board;

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    board = new int[n][n];
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        board[i][j] = sc.nextInt();
      }
    }

    int maxCount = 0;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n - 2; j++) {
        maxCount = Math.max(maxCount, board[i][j] + board[i][j + 1] + board[i][j + 2]);
      }
    }
    System.out.println(maxCount);
  }

}