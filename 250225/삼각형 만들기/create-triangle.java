import java.util.*;

public class Main {

  static int[][] points;
  static int result;

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    points = new int[n][2];

    for (int i = 0; i < n; i++) {
      points[i][0] = sc.nextInt(); //x point
      points[i][1] = sc.nextInt(); //y point
    }

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        for (int k = 0; k < n; k++) {
          if (i == j || j == k || k == i) {
            continue;
          }

          calculatePoints(i, j, k);
        }
      }
    }
    System.out.println(result);

  }

  private static void calculatePoints(int i, int j, int k) {
    boolean sameXaxios = points[i][1] == points[j][1];
    boolean sameYaxios = points[j][0] == points[k][0];
    if (sameXaxios && sameYaxios) {
      result = Math.max(result,
          (Math.abs(points[i][0] - points[j][0]) * Math.abs(points[j][1] - points[k][1])));
    }
  }


}
