class Solution {

    private static int[] memo;

    public int coinChange(int[] coins, int amount) {
        memo = new int[amount + 1];

        Arrays.fill(memo, -1);
        int answer = dfs(amount, coins);
        return answer == Integer.MAX_VALUE ? -1 : answer;
    }

    private int dfs(int target, int[] coins) {

        if (target == 0) {
            return 0;
        }

        if (target < 0) {
            return Integer.MAX_VALUE;
        }

        if (memo[target] != -1) {
            return memo[target];
        }

        int minCnt = Integer.MAX_VALUE;

        for (int coin : coins) {
            // 11 - 1 = 10 을 만드는 최수 동전 수 ,
            // 11 - 2 = 9 을 만드는 최수 동전 수 ,
            // 11- 5 = 9을 만드는 최소 동전 수
            int cnt = dfs(target - coin, coins);

            if (cnt != Integer.MAX_VALUE) {
                minCnt = Math.min(minCnt, cnt + 1);
            }
        }

        memo[target] = minCnt;
        return memo[target];
    }
}
