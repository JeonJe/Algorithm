

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int[] num = new int[n];

    for (int i = 0; i < n; i++) {
      num[i] = sc.nextInt();
    }
    int maxCount = 1;
    int count = 1;
    for (int i = 0; i < n; i++) {
      if (i == 0 || num[i - 1] != num[i]) {
        count = 1;
        continue;
      }
      count++;
      if (count > maxCount) {
        maxCount = count;
      }
    }
    System.out.println(maxCount);

  }

}


