import java.util.*;

public class Main {

  private static final int OP_TIME_SIZE = 1001;
  static int[][] workTimes;
  static int[] optimes = new int[OP_TIME_SIZE];
  static int maxOpTime;

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int n = sc.nextInt();
    workTimes = new int[n][2];
    for (int i = 0; i < n; i++) {
      int from = sc.nextInt();
      int to = sc.nextInt();
      workTimes[i] = new int[]{from, to};
    }

    for (int i = 0; i < n; i++) {
      hire(i);
    }

    for (int i = 0; i < n; i++) {
      fire(i);
      maxOpTime = Math.max(maxOpTime, countOpTimes());
      hire(i);
    }

    System.out.println(maxOpTime);
  }

  private static void fire(int i) {
    for (int j = workTimes[i][0]; j < workTimes[i][1]; j++) {
      optimes[j]--;
    }
  }

  private static void hire(int i) {
    for (int j = workTimes[i][0]; j < workTimes[i][1]; j++) {
      optimes[j]++;
    }
  }

  private static int countOpTimes() {
    int optimeCount = 0;
    for (int k = 0; k < OP_TIME_SIZE; k++) {
      if (optimes[k] > 0) {
        optimeCount++;
      }
    }
    return optimeCount;
  }

}
