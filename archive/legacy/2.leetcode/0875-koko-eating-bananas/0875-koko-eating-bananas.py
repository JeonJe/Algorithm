class Solution:
    def check(self, mid, piles, h):
        spend = 0 
        for i in range(len(piles)):
            q = piles[i] // mid
            r = piles[i] % mid
            
            if r > 0:
                q += 1
            spend += q
            
        return spend <= h
            
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 0
        right = 10**9
        
        while left+1 < right:
            mid = left + ((right - left) // 2)
            
            if self.check(mid, piles, h):
                right = mid
            else:
                left = mid
        
        return right
        