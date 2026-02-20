import java.util.Scanner;

public class Main {

  public static int[] lines = new int[201];

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();

    for (int i = 0; i < n; i++) {
      int from = sc.nextInt() + 100;
      int to = sc.nextInt() + 100;
      draw(from, to);
    }

    int maxOverrlapped = 0;
    for (int i = 0; i < 201; i++) {
      if (lines[i] > maxOverrlapped) {
        maxOverrlapped = lines[i];
      }
    }
    System.out.println(maxOverrlapped);
  }


  public static void draw(int from, int to) {
    for (int i = from; i < to; i++) {
      lines[i]++;
    }
  }
}


