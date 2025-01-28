import java.util.*;

public class Main {

  public static final int MAX_BOARD_SIZE = 2001;
  public static int[][] board = new int[MAX_BOARD_SIZE][MAX_BOARD_SIZE];
  public static Squre A;
  public static Squre B;
  public static Squre M;

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    A = inputFrom(sc);
    B = inputFrom(sc);
    M = inputFrom(sc);

    draw(A, 1);
    draw(B, 1);
    draw(M, 0);

    int area = 0;
    for (int i = 0; i < MAX_BOARD_SIZE; i++) {
      for (int j = 0; j < MAX_BOARD_SIZE; j++) {
        if (board[i][j] == 1) {
          area++;
        }
      }
    }
    System.out.println(area);
  }

  private static void draw(Squre a, int num) {
    for (int x = a.leftBottomX; x < a.rightTopX; x++) {
      for (int y = a.leftBottomY; y < a.rightTopY; y++) {
        board[x][y] = num;
      }
    }
  }

  private static Squre inputFrom(Scanner sc) {
    int leftBottomX = sc.nextInt() + 1000;
    int leftBottomY = sc.nextInt() + 1000;
    int rightTopX = sc.nextInt() + 1000;
    int rightTopY = sc.nextInt() + 1000;
    return new Squre(leftBottomX, leftBottomY, rightTopX, rightTopY);
  }

  public static class Squre {

    int leftBottomX;
    int leftBottomY;
    int rightTopX;
    int rightTopY;

    public Squre(int leftBottomX, int leftBottomY, int rightTopX, int rightTopY) {
      this.leftBottomX = leftBottomX;
      this.leftBottomY = leftBottomY;
      this.rightTopX = rightTopX;
      this.rightTopY = rightTopY;
    }
  }

}


