class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        board =  [ [] for _ in range(numRows) ]
        
        row = 0
        down = True
        
        for i in range(len(s)):
            board[row].append(s[i])
            if row == 0:
                down = True
            elif row == numRows - 1:
                down = False
            
            if down:
                row += 1
            else:
                row -= 1
        
        answer = ''
        for r in range(numRows):
            answer += ''.join(board[r])
        return answer
                
            