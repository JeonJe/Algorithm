class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        if(n <= 0) {
            return 0;
        }
        if(n == 1) {
            return nums[0];
        }
        if(n == 2) {
            return Math.max(nums[0], nums[1]);
        }
        
        // 각 집까지 털었을 때 최대 금액
        int[] dp = new int[101];

        dp[0] = nums[0];
        //첫 번째 집을 털던지, 두 번째 집을 털던지
        dp[1] = Math.max(nums[0], nums[1]);
        int answer = 0;

        for(int i = 2; i < n; i++) {
            // 바로 전집 건너뛰고, 2번째전 집까지 털고 이번집 털기 vs 이번집 포기하기 바로 전집까지 털어먹기 
            dp[i] = Math.max(dp[i-2] + nums[i], dp[i-1]);
            answer = Math.max(answer, dp[i]);
        }

        return answer;

    }
}