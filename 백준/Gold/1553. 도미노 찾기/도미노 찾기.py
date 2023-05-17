
height = 8 
width = 7

board = [ list(map(int,input())) for _ in range(height) ]
visited = [ [False for _ in range(width)] for _ in range(height) ]
used = [ [False for _ in range(7)] for _ in range(7)]  # 00 to 66


def backtracking(x,y):
    
    if x >= height:
        return 1
    
    cnt = 0
    nx, ny = x, y + 1
    if ny >= width:
        nx,ny = x+1, 0
    
    if visited[x][y]:
        return backtracking(nx,ny)    
    else:
        visited[x][y] = True
        head = board[x][y]
   
        for dx,dy in [(0,1),(1,0)]:
            mx = x + dx
            my = y + dy 
            
            if 0 <= mx < height and 0 <= my < width:
                tail = board[mx][my]
                
                if not visited[mx][my] and not used[head][tail]:
                    visited[mx][my] = True
                    used[head][tail], used[tail][head] = True, True
                    cnt += backtracking(nx,ny)
                    visited[mx][my] = False
                    used[head][tail], used[tail][head] = False, False

        visited[x][y] = False
        return cnt


print(backtracking(0,0))
