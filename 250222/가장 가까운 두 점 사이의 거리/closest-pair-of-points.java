

import java.util.*;

public class Main {

  static int[][] points;

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    points = new int[n][2];
    for (int i = 0; i < n; i++) {
      int x = sc.nextInt();
      int y = sc.nextInt();
      points[i] = new int[]{x, y};
    }

    int minDistance = Integer.MAX_VALUE;
    for (int i = 0; i < n; i++) {
      for (int j = i + 1; j < n; j++) {
        minDistance = Math.min(minDistance, getDistance(points[i], points[j]));
      }
    }
    System.out.println(minDistance);
  }

  private static int getDistance(int[] point1, int[] point2) {
    return (int) (Math.pow(Math.abs(point1[0] - point2[0]), 2) + Math.pow(
        Math.abs(point1[1] - point2[1]), 2));
  }


}
