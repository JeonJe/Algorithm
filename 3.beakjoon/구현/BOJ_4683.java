import java.util.*;
import java.io.*;

public class BOJ_4683 {
  static boolean[] check = new boolean[10036];
  public static void main(String[] args) throws Exception {
    for (int i = 1; i < 10001; i++) {
      check[d(i)] = true;
    }
    StringBuilder sb = new StringBuilder();
    for (int i = 1; i < 10001; i++) {
      if (!check[i]) {
        sb.append(i);
        sb.append('\n');
      }
    }
    System.out.println(sb.toString());

  }
  static int d(int n) {
    int sumN = n;
    while (n > 0) {
      sumN = sumN + n % 10;
      n = (int)(n / 10);
    }
    return sumN;
  }


}
