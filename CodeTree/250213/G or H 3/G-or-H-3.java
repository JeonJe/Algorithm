import java.util.Scanner;

public class Main {

  static int MAX_SIZE = 10_001;

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int k = sc.nextInt();

    int[] arr = new int[MAX_SIZE];

    for (int i = 0; i < n; i++) {
      int position = sc.nextInt();
      char alphabet = sc.next().charAt(0);
      if (alphabet == 'G') {
        arr[position] = 1;
      } else {
        arr[position] = 2;
      }
    }
    int result = 0;
    for (int i = 1; i < MAX_SIZE - k; i++) {
      int currentPoints = 0;
      for (int j = i; j <= i + k; j++) {
        currentPoints += arr[j];
      }
      result = Math.max(result, currentPoints);
    }
    System.out.println(result);
  }

}
