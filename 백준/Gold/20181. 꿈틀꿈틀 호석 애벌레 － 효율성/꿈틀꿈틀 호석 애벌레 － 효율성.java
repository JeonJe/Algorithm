import java.util.*;
import java.io.*;

class Main {
  public static void main(String[] args) throws Exception {

    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(reader.readLine());

    int N = Integer.parseInt(st.nextToken());
    int K = Integer.parseInt(st.nextToken());

    int[] seq = new int[N];
    st = new StringTokenizer(reader.readLine());
    for (int i = 0; i < N; i++) {
      seq[i] = Integer.parseInt(st.nextToken());
    }
    long[] dp = new long[N+1];
    long prefixSum = seq[0];
    int left = 0; 
    int right = 1;

    while (right <= N) {
      if (prefixSum >= K) {
        while (prefixSum >= K){
          dp[right] = Math.max(dp[right], dp[left] + prefixSum - K);
          prefixSum -= seq[left];
          left++;
        }
      } else {
        dp[right] = Math.max(dp[right], dp[right-1]);
        if (right == N) {
          break;
        }
        prefixSum += seq[right];
        right++;
      }
    }
    System.out.println(dp[N]);

  }
}