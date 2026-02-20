import java.util.Scanner;

public class Main {

  static int n;
  static int m;
  static int k;

  static int[] students;
  static int[] penalties;
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    n = sc.nextInt();
    students = new int[n];
    m = sc.nextInt();
    penalties = new int[m];
    k = sc.nextInt();

    for(int i = 0; i < m; i++) {
      int penaltyTarget = sc.nextInt();
      penalties[penaltyTarget - 1]++;
      if(penalties[penaltyTarget - 1] == k) {
        System.out.println(penaltyTarget);
        return;
      }
    }
    System.out.println(-1);


  }
}


