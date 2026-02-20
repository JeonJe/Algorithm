
import java.util.*;

public class Main {

  static int[] dx = {0, 0, 1, -1};
  static int[] dy = {1, -1, 0, 0};
  static int cx = 0;
  static int cy = 0;

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    for (int i = 0; i < n; i++) {
      String dir = sc.next();
      int d = sc.nextInt();
      move(dir, d);
    }

    System.out.println(cx + " " + cy);
  }

  public static void move(String dir, int d) {
    for (int i = 0; i < d; i++) {
      if ("N".equals(dir)) {
        cx += dx[0];
        cy += dy[0];
      }
      if ("S".equals(dir)) {
        cx += dx[1];
        cy += dy[1];

      }
      if ("E".equals(dir)) {
        cx += dx[2];
        cy += dy[2];

      }
      if ("W".equals(dir)) {
        cx += dx[3];
        cy += dy[3];
      }
    }
  }
}
