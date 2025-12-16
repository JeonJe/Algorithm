class Solution {
    public int maxProfit(int[] prices) {
       int n = prices.length;
       if(n < 2) {
        return 0;
       }

       int minBuyPrice = prices[0];
       int maxProfit = 0; 

       for(int i = 0; i < n; i++) {
        //최소 구매가격 - 지금 판매 가격이 최대인지 계산 
            maxProfit = Math.max(maxProfit, prices[i] - minBuyPrice);
            //오늘이 최소 구매 가격일 수도 있어!
            minBuyPrice = Math.min(minBuyPrice, prices[i]);
       }

       return maxProfit;


    }
}