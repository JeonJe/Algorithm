
import java.util.*;

public class Main {

  private static final int OFFSET = 100;
  static int MAX_BOARD_SIZE = 201;
  public static int[][] board = new int[MAX_BOARD_SIZE][MAX_BOARD_SIZE];

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int numOfCommand = sc.nextInt();

    for (int i = 1; i <= numOfCommand; i++) {
      int leftBottomX = sc.nextInt() + OFFSET;
      int leftBottomY = sc.nextInt() + OFFSET;
      int rightTopX = sc.nextInt() + OFFSET;
      int rightTopY = sc.nextInt() + OFFSET;

      int color = 1;
      //파랑
      if (i % 2 == 0) {
        color = 2;
      }

      draw(leftBottomX, leftBottomY, rightTopX, rightTopY, color);
    }

    int blueCount = 0;
    for (int i = 0; i < MAX_BOARD_SIZE; i++) {
      for (int j = 0; j < MAX_BOARD_SIZE; j++) {
        if (board[i][j] == 2) {
          blueCount++;
        }
      }
    }
    System.out.print(blueCount);
  }

  private static void draw(int leftBottomX, int leftBottomY, int rightTopX, int rightTopY,
      int color) {

    for (int i = leftBottomX; i < rightTopX; i++) {
      for (int j = leftBottomY; j < rightTopY; j++) {
        board[i][j] = color;
      }
    }
  }


}
