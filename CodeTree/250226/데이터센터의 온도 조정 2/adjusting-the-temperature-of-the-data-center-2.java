import java.util.Scanner;

public class Main {

  static int MINIMUM_DEGREE = 0;
  static int MAXIMUM_DEGREE = 1000;
  static int c;
  static int g;
  static int h;

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    c = sc.nextInt();
    g = sc.nextInt();
    h = sc.nextInt();
    int[] ta = new int[n];
    int[] tb = new int[n];
    for (int i = 0; i < n; i++) {
      ta[i] = sc.nextInt();
      tb[i] = sc.nextInt();
    }

    int maxWork = 0;
    for (int curDegree = MINIMUM_DEGREE; curDegree <= MAXIMUM_DEGREE; curDegree++) {
      int sumOfWork = 0;
      for (int i = 0; i < n; i++) {
        int work = calcaulteWork(ta[i], tb[i], curDegree);
        sumOfWork += work;
      }
      maxWork = Math.max(maxWork, sumOfWork);
    }
    System.out.println(maxWork);

  }

  private static int calcaulteWork(int ta, int tb, int curDegree) {
    if (curDegree < ta) {
      return c;
    }
    if (curDegree > tb) {
      return h;
    }
    return g;
  }
}
