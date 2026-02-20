import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int[] a = new int[n];
    int[] b = new int[n];
    int[] c = new int[n];
    for (int i = 0; i < n; i++) {
      a[i] = sc.nextInt();
      b[i] = sc.nextInt();
      c[i] = sc.nextInt();
    }
    // Please write your code here.

    int maxCount = 0;

    for(int firstStoneIndex = 0; firstStoneIndex < 3; firstStoneIndex++) {
      int count = 0;
      // 처음 조약돌의 위치 i
      int[] cups= new int[3];
      cups[firstStoneIndex] = 1;
      for(int j = 0; j < n; j++) {
        int swapA = a[j] - 1;
        int swapB = b[j] - 1;

        int temp = cups[swapA];
        cups[swapA] = cups[swapB];
        cups[swapB] = temp;

        int openCup = c[j] - 1;
        if(cups[openCup] == 1) {
          count++;
        }
      }
      maxCount = Math.max(maxCount, count);
    }
    System.out.println(maxCount);
  }
}
