import java.util.*;

public class Main {

  public static int[] blocks;
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    blocks = new int[n+1];

    int k = sc.nextInt();

    for(int i = 0; i < k; i++) {
      int from = sc.nextInt();
      int to = sc.nextInt();
      draw(from, to);
    }
    int maxValue = 0;
    for(int i = 0; i < n; i++) {
      if(blocks[i] > maxValue) {
        maxValue = blocks[i];
      }
    }
    System.out.println(maxValue);
  }

  private static void draw(int from, int to) {
    for(int i = from; i <= to; i++) {
      blocks[i] += 1;
    }
  }
}

