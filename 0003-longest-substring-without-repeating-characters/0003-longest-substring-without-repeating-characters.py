from collections import defaultdict 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        answer = 1
        n = len(s)
        l, r = 0, 0
        
        visited = set()
        
        while l < n and r < n:
            if s[r] not in visited:
                visited.add(s[r])
                answer = max(answer, r-l+1)
                r += 1
            else:
                visited = set()
                l +=1
                r = l
                
        return answer
            