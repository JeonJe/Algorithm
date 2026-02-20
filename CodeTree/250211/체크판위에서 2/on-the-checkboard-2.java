
import java.util.Scanner;

public class Main {

  static int[][] board;
  static int rowCount;
  static int columnCount;
  static int result;

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
     rowCount = scanner.nextInt();
     columnCount = scanner.nextInt();
    board = new int[rowCount][columnCount];

    for(int i = 0; i < rowCount; i++) {
      for(int j = 0; j < columnCount; j++) {
        String cur = scanner.next();
        if(cur.equals("B")) {
          board[i][j] = 1;
        }
      }
    }

    int currentColor = board[0][0];
    int jumpCount = 3;

    jump(0,0, currentColor, jumpCount);
    System.out.println(result);
  }

  private static void jump(int curRow, int curCol, int currentColor, int jumpCount) {
    if(curRow == rowCount - 1 && curCol == columnCount - 1 && jumpCount == 0) {
        result++;
      return;
    }
    
    if(jumpCount == 0) {
      return;
    }

    for(int i = curRow+1; i < rowCount; i++) {
      for(int j = curCol+1; j < columnCount; j++) {
          if(board[i][j] != currentColor && jumpCount > 0) {
            jumpCount--;

            currentColor = flipColor(currentColor);
            jump(i, j, currentColor, jumpCount);
            jumpCount++;
            currentColor = flipColor(currentColor);

          }
      }
    }
  }

  private static int flipColor(int color) {
    if(color == 0) {
      return 1;
    }
      return 0;
  }

}