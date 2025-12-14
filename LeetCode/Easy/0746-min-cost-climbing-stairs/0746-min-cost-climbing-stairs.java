import java.util.*;

class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int n = cost.length;
        if(n == 2) {
            return Math.min(cost[0], cost[1]);
        }
        //i까지 최소 비용 
        int[] dp = new int[1001];
        dp[0] = cost[0];
        dp[1] = cost[1];

        for(int i = 2; i < n; i++) {
            dp[i] = Math.min(dp[i-2], dp[i-1]) + cost[i];
        }

        return Math.min(dp[n-1], dp[n-2]);

    }
}