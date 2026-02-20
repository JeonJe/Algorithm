
import java.util.Scanner;

public class Main {

  public static int[] dx = {0, 1, 0, -1};
  public static int[] dy = {1, 0, -1, 0};
  public static int direction = 0;
  public static int cx = 0;
  public static int cy = 0;

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String inputs = sc.nextLine();
    for (char c : inputs.toCharArray()) {
      if (c == 'L' || c == 'R') {
        rotate(c);

      } else {
        move();
      }
    }
    System.out.printf("%d %d", cx, cy);
  }

  public static void rotate(char c) {
    if (c == 'L') {
      direction = (direction + 3) % 4;
    } else {
      direction = (direction + 1) % 4;
    }
  }

  public static void move() {
    cx += dx[direction];
    cy += dy[direction];
  }

}
