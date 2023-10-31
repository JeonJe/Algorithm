class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        cnt =  {}
        maxf = 0
        
        for r in range(len(s)):
            cnt[s[r]] = cnt.get(s[r], 0) + 1
            maxf = max(maxf, cnt[s[r]])
            #sliding window lenght - most freq chracter count > k
            while (r - l + 1) - maxf > k:
                cnt[s[l]] -= 1
                l += 1
                
            
        return r - l + 1

