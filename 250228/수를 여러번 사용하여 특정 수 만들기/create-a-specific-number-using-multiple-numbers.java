import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int a = sc.nextInt();
    int b = sc.nextInt();
    int c = sc.nextInt();


    int maxSumValue = 0;
    for(int i = 0; i <= 1000; i ++) {
      for(int j = 0; j <= 1000; j++) {
        if(a * i + b * j <= c) {
          maxSumValue = Math.max(maxSumValue, a * i + b * j);
        }
      }
    }
    System.out.println(maxSumValue);
  }
}
