
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    // Please write your code here.
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();

    System.out.print(F(n));
  }

  public static int F(int num) {
    if (num < 10) {
      return (int) Math.pow(num, 2);
    }

    return F(num / 10) + (int) Math.pow((num % 10), 2);
  }
}

