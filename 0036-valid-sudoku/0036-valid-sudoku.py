class Solution:
    
    def validate_sudoku(self, board, x, y, length):
        #row 확인
        for i in range(length):
            if i == y:
                continue
            if board[x][i] == board[x][y]:
                print("row", x,i)
                return False
        #col 확인
        for i in range(length):
            if i == x :
                continue
            if board[i][y] == board[x][y]:                
                print("col", i,y)
                return False
            
        #3x3 확인
        sub_box_x = (x // 3) * 3
        sub_box_y = (y // 3) * 3
        print(sub_box_x, sub_box_y)
        for i in range(sub_box_x, sub_box_x+3):
            for j in range(sub_box_y, sub_box_y+3):
                if i == x and j == y:
                    continue
                if board[i][j] == board[x][y]:
                    print("3x3   false",  x, y, board[x][y])
                    return False
                
        return True
        
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        length = len(board)
        for i in range(length):
            for j in range(length):
                print(i,j)
                if board[i][j] != ".":
                    if not self.validate_sudoku(board, i, j, length):
                        return False
        
        return True
