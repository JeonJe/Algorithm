import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int s = sc.nextInt();

    int[] arr = new int[n];

    int initSum = 0;
    for (int i = 0; i < n; i++) {
      arr[i] = sc.nextInt();
      initSum += arr[i];
    }

    int minDiff = Integer.MAX_VALUE;

    for (int i = 0; i < n - 1; i++) {
      for (int j = i + 1; j < n; j++) {
        int currentSum = initSum - arr[i] - arr[j];
        minDiff = Math.min(minDiff, Math.abs(s - currentSum));
      }
    }
    System.out.println(minDiff);
  }
}
