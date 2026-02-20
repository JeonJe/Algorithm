
import java.util.Scanner;

public class Main {

  private static int MAX_TIME = 1_000_000;
  static int[] timeLineA = new int[MAX_TIME];
  static int[] timeLineB = new int[MAX_TIME];

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int moveACount = sc.nextInt();
    int moveBCount = sc.nextInt();

    int currentTime = 1;
    for (int i = 0; i < moveACount; i++) {
      String direction = sc.next();
      int time = sc.nextInt();
      for (int j = currentTime; j < currentTime + time; j++) {
        if ("R".equals(direction)) {
          timeLineA[j] = timeLineA[j - 1] + 1;
        } else {
          timeLineA[j] = timeLineA[j - 1] - 1;
        }
      }
      currentTime += time;
    }
    int maxTime = currentTime;
    currentTime = 1;
    for (int i = 0; i < moveBCount; i++) {
      String direction = sc.next();
      int time = sc.nextInt();
      for (int j = currentTime; j < currentTime + time; j++) {
        if ("R".equals(direction)) {
          timeLineB[j] = timeLineB[j - 1] + 1;
        } else {
          timeLineB[j] = timeLineB[j - 1] - 1;
        }
      }
      currentTime += time;
    }

    print(maxTime);
  }

  private static void print(int maxTime) {
    for (int i = 1; i < maxTime; i++) {
      if (timeLineA[i] == timeLineB[i]) {
        System.out.println(i);
        return;
      }
    }
    System.out.println(-1);
  }
}


