class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrix_height = len(matrix)
        matrix_width = len(matrix[0])
        
        #첫번째 column의 값으로 lower bound 의 위치를 찾음
        bot, top = 0, matrix_height-1
        row = 0
        
        while bot <= top:
            row = (bot + top)//2
            
            if matrix[row][0] >  target:
                top = row - 1
            elif matrix[row][-1] < target:
                bot = row + 1
            else:
                break
        if not (bot <= top):
            return False

        
        rows = matrix[row]
        l, r = 0, len(rows)-1
        
        while l <= r:
            m = l + ((r - l) // 2)
            if rows[m] == target:
                return True
            elif rows[m] < target:
                l = m + 1
            else:
                r = m - 1
 
        return False

        
        