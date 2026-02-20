
import java.util.*;

public class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int n = sc.nextInt();
    // 0 은 x 좌표, 1 은 y 좌표
    int[][] arr = new int[n][2];

    for (int i = 0; i < n; i++) {
      arr[i][0] = sc.nextInt();
      arr[i][1] = sc.nextInt();
    }

    int minArea = Integer.MAX_VALUE;

    //좌표 중 1개 점 빼기
    for (int i = 0; i < n; i++) {

      int minX = Integer.MAX_VALUE;
      int maxX = 0;
      int minY = Integer.MAX_VALUE;
      int maxY = 0;
      for (int j = 0; j < n; j++) {
        if (i == j) {
          continue;
        }
        minX = Math.min(minX, arr[j][0]);
        maxX = Math.max(maxX, arr[j][0]);
        minY = Math.min(minY, arr[j][1]);
        maxY = Math.max(maxY, arr[j][1]);
      }
      //모든 점들을 포함하는 직사각형 넓이 구하기
      int area = (maxX - minX) * (maxY - minY);
      minArea = Math.min(minArea, area);
    }
    System.out.println(minArea);
  }

}
