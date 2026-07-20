class Solution {

    public int maxProfit(int[] prices) {
        int n = prices.length;
        int maxProfit = 0;
        int minPrice = prices[0];

        for (int buyDay = 1; buyDay < n; buyDay++) {
            minPrice = Math.min(minPrice, prices[buyDay]);
            maxProfit = Math.max(maxProfit, prices[buyDay] - minPrice);
        }
        
        return maxProfit;
    };
}
