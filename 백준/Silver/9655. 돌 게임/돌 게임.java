import java.util.*;
import java.io.*;

public class Main {
  public static void main(String[] args) throws Exception {
    BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));

    int N = Integer.parseInt(rd.readLine());
    //N일 때 최소 턴의 수
    int[] dp = new int[1001];

    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 1;

    for (int i = 4; i < N+1; i++) {
      dp[i] = Math.min(dp[i-1], dp[i-3])+1;
    }
    if (dp[N] % 2 == 0) {
      System.out.println("CY");
    } else {
      System.out.println("SK");
    }
  }
}
