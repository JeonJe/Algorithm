class Solution:
    def lengthOfLastWord(self, s: str) -> int:
      
      splited_s = s.split()

      return len(splited_s[-1])