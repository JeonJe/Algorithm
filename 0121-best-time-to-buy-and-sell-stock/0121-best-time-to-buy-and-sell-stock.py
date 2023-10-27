class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        l,r = 0,0
        profit = 0
        while l < length:
            profit = max(profit, prices[r] - prices[l])
            #r포인터가 가리키는 값이 l포인터가 가리키는 값보다 크면
            #r을 증가시킴
            if prices[r]>= prices[l]:
                r += 1
                if r >= length:
                    break
            else:
                l = r
                r = l
            
                
        return profit