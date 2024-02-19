class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        int left = 0;
        int right = 1;
        
        while(left < prices.length && right < prices.length){
            int profit = prices[right] - prices[left];
            if(profit >= 0){
                maxProfit = Math.max(maxProfit, profit);
                right++;
            } else {
                left++;
                right = left+1;
            }
            
        }
        return maxProfit;
    }
}