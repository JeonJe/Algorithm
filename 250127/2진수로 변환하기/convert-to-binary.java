import java.util.*;

public class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();

    convertToBinary(n);
  }

  private static void convertToBinary(int n) {
    int[] binary = new int[32];
    int count = 0;
    while (true) {
      if (n < 2) {
        binary[count++] = n;
        break;
      }
      binary[count] = n % 2;
      count++;
      n = n / 2;
    }

    for (int i = count - 1; i >= 0; i--) {
      System.out.print(binary[i]);
    }
  }


}

