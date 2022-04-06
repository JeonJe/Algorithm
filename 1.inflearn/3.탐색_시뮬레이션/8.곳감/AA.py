
import sys
# sys.stdin = open("input.txt",'rt')

N = int(input())

res = 0
arr = [ list(map(int,input().split())) for _ in range(N)]

#왼, 위, 오, 아 
dx = [-1,0,1,0]
dy = [0,-1,0,1]


for i in range(N):
    for j in range(N):
        cur = arr[i][j]
        point = True

        for z in range(4):
            nx = j+dx[z] 
            ny = i+dy[z]

            if nx < 0 or nx >= N or ny < 0 or ny >= N :
                continue
            
            if arr[ny][nx] >= cur:
                point = False

        if point:
            res += 1
        


print(res)