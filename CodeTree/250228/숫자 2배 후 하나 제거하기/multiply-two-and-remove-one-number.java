import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int[] arr = new int[n];
    for (int i = 0; i < n; i++) {
      arr[i] = sc.nextInt();
    }
    // Please write your code here.

    int minDiffSum = Integer.MAX_VALUE;
    for (int multipleIndex = 0; multipleIndex < n; multipleIndex++) {
      //하나의 수 선택
      arr[multipleIndex] = arr[multipleIndex] * 2;

      int[] remainingArr = new int[n - 1];
      //제거할 하나의 수 선택
      for (int removeIndex = 0; removeIndex < n; removeIndex++) {
        if (multipleIndex == removeIndex) {
          continue;
        }
        int count = 0;
        for (int copyIndex = 0; copyIndex < n; copyIndex++) {
          if (copyIndex == removeIndex) {
            continue;
          }
          remainingArr[count++] = arr[copyIndex];
        }

        int sum = 0;
        for (int i = 1; i < n - 1; i++) {
          sum += Math.abs(remainingArr[i] - remainingArr[i - 1]);
        }
        minDiffSum = Math.min(minDiffSum, sum);


      }

      arr[multipleIndex] = arr[multipleIndex] / 2;
    }
    System.out.println(minDiffSum);
  }
}
