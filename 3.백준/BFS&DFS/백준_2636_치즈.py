
import sys
from collections import deque

# sys.stdin = open("input.txt",'rt')


dy = [ 1,0,-1,0]
dx = [ 0,1,0,-1]

def bfs(x):

    while deq:
        cur = deq.popleft()
        for i in range(4):
            #세로 
            ny = cur[0] + dy[i]
            #가로
            nx = cur[1] + dx[i]
            
            if 0<= ny < height and 0<= nx < width and visited[ny][nx] == 0:
                visited[ny][nx] = 1

                #치즈의 가장 자리라면?
                if Map[ny][nx] == 1:
                    
                    Map[ny][nx] = 2
                    x-=1
                else:
                    deq.append([ny,nx])

    return x

def delete():
    for i in range(height):
        for j in range(width):
            if Map[i][j] == 2:
                Map[i][j] == 0


height, width = map(int,input().split(" "))
Map =[]

for _ in range(height):
    Map.append(list(map(int,input().split(" "))))

Left = 0

for i in range(height):
    for j in range(width):
        if Map[i][j] == 1:
            Left+=1

deq = deque()
cnt = 0
temp = Left

while Left != 0 :
    visited = [ [0 for _ in range(width)] for _ in range(height)]
    deq.append([0,0])
    visited[0][0] = 1
    Left = bfs(Left)

    if Left !=0:
        temp = Left

    cnt+=1
    delete()

print(cnt)
print(temp)