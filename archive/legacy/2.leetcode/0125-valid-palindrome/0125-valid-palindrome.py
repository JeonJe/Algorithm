class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ''
        
        for char in s:
            if char.isupper():
                temp += char.lower()
            elif char.islower() or char.isnumeric():
                temp += char
        # print(temp)
        return temp == temp[::-1]
        