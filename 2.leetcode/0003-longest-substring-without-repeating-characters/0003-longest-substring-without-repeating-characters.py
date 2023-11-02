from collections import defaultdict 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l, answer = 0, 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            answer = max(answer, r - l + 1)
                
        return answer
            