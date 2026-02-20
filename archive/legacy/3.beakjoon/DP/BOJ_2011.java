import java.io.*;

class BOJ_2011 {
  static final int MOD = 1000000;
  public static void main(String[] args) throws Exception {
      BufferedReader reader = new BufferedReader ( new InputStreamReader(System.in));
      String num = reader.readLine();

      if (num.charAt(0) == '0') {
        System.out.println(0);
        return ;
      }
      
      int n = num.length();
      int[] dp = new int[n+1];
      dp[0] = 1;
      dp[1] = 1;
      
      for (int i = 2; i < n+1; i++) {
        
        if ( num.charAt(i-1) != '0') {
          dp[i] = (dp[i-1] + dp[i] ) % MOD;
        }
        int previousTwoDigitsNum = Character.getNumericValue(num.charAt(i-2))*10+Character.getNumericValue(num.charAt(i-1));
        if (10<= previousTwoDigitsNum && previousTwoDigitsNum <= 26) {
          dp[i] = (dp[i-2] + dp[i] ) % MOD;
        }
      }
      System.out.println(dp[n]);
      
      return ;
  }
}