import java.util.Scanner;

public class Main {

  static int result;

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int x = sc.nextInt();
    int y = sc.nextInt();
    
    for (int i = x; i <= y; i++) {
      int sum = sumDigit(i);
      result = Math.max(result, sum);
    }
    System.out.println(result);
  }

  private static int sumDigit(int i) {
    int sum = 0;
    while (i >= 10) {
      sum += i % 10;
      i = i / 10;
    }
    sum += i;
    return sum;
  }
}
