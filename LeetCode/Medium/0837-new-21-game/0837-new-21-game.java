class Solution {
    public double new21Game(int n, int k, int maxPts) {
        if(k == 0) {
            return 1.0;
        }
        if(n >= k + maxPts) {
            return 1.0;
        }

        double[] dp = new double[k + maxPts];

        for(int i = k; i <= n && i < k + maxPts; i++) {
            dp[i] = 1.0;
        }

        double sum = 0;
        for(int i = k; i < k + maxPts; i++) {
            sum += dp[i];
        }

        for(int i = k -1; i >=0; i--) {
            dp[i] = sum / maxPts;
            sum = sum - dp[i + maxPts] + dp[i];
        }

        return dp[0];
       
    }
}