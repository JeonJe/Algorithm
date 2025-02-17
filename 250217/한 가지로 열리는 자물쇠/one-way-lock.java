
import java.util.Scanner;

public class Main {


  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int[] arr = new int[n];

    for (int i = 0; i < 3; i++) {
      arr[i] = sc.nextInt();
    }

    int count = 0;
    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= n; j++) {
        for (int k = 1; k <= n; k++) {
          if (Math.abs(i - arr[0]) <= 2
              || Math.abs(j - arr[1]) <= 2 ||
              Math.abs(k - arr[2]) <= 2) {
            count++;
          }

        }
      }
    }
    System.out.println(count);
  }

}
