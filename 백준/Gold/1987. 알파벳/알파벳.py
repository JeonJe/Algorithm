import sys
input = sys.stdin.readline

height, width = map(int,input().split())
board = [list(input().rstrip()) for _ in range(height)]
used_alpha = [False]*26

answer = 0
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def dfs(cx,cy,cnt,used_alpha):
    global answer
    
    answer = max(answer, cnt)
    if answer == 26:
        print(26)
        exit(0)

    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if 0 > nx or nx >= height or 0 > ny or ny >= width:
             continue
        
        alpha = ord(board[nx][ny])-ord('A')
        if not used_alpha[alpha]:
                used_alpha[alpha] = True
                dfs(nx,ny,cnt+1,used_alpha)
                used_alpha[alpha] = False


used_alpha[ord(board[0][0])-ord('A')] = True
dfs(0,0,1,used_alpha)
print(answer)

