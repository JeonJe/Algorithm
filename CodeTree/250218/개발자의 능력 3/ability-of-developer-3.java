import java.util.*;

public class Main {

  private static final int STUDENTS_SIZE = 6;
  static int total = 0;
  static int[] arr;

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    arr = new int[STUDENTS_SIZE];
    for (int i = 0; i < STUDENTS_SIZE; i++) {
      arr[i] = sc.nextInt();
      total += arr[i];
    }

    int minDiff = Integer.MAX_VALUE;

    for (int i = 0; i < STUDENTS_SIZE - 2; i++) {
      for (int j = i + 1; j < STUDENTS_SIZE - 1; j++) {
        for (int k = j + 1; k < STUDENTS_SIZE; k++) {
          minDiff = Math.min(minDiff, getDiff(i, j, k));
        }
      }
    }
    System.out.println(minDiff);

  }

  private static int getDiff(int i, int j, int k) {
    int sum1 = arr[i] + arr[j] + arr[k];
    int sum2 = total - sum1;
    return Math.abs(sum1 - sum2);
  }
}