import sys
from collections import defaultdict 
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N, M, K = map(int,input().split())
board = [list(input().rstrip()) for _ in range(N)]
str_map = defaultdict(int)

dx = [1,1,0,-1,-1,-1,0,1]
dy = [0,-1,-1,-1,0,1,1,1]

def dfs(x,y,depth,path):
    if depth == 5:
        return

    str_map[path] += 1
        
    for i in range(8):
        nx = (x + dx[i] + N) % N 
        ny = (y + dy[i] + M) % M    
        dfs(nx, ny, depth+1, path + board[nx][ny])

for i in range(N):
  for j in range(M):
    dfs(i,j,0,board[i][j])

for i in range(K):
    target = input().rstrip()
    print(str_map[target])