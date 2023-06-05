import sys

input = sys.stdin.readline

n = int(input())
seq = [list(map(int,input().split())) for _ in range(n)]
origin = list(map(int,input().split()))
visited = [False] * (n)

#depth : 몇개 물감 선택했는지
#idx : 현재 확인중인 물감 위치 
def dfs(depth, idx, r,g,b):
    global answer

    if depth >= 2:
        temp_r,temp_g,temp_b = r//depth, g//depth, b//depth
        diff = abs(origin[0] - temp_r) + abs(origin[1] - temp_g) + abs(origin[2] - temp_b)
        answer = min (answer, diff)
        
    for i in range(idx+1,n):
        if depth < 7:
            dfs(depth+1, i, r+seq[i][0], g+seq[i][1], b+seq[i][2])

global answer 
answer = 1e9

dfs(0,-1,0,0,0)
print(answer)