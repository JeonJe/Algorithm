import sys
from collections import deque

input = sys.stdin.readline
R,C = map(int,input().split())
graph = [ list(input().rstrip()) for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

global end_point 
global cnt 
cnt = 0

hedgehog = deque()
water = deque()

def bfs():
    global cnt 
    while hedgehog: 
        for i in range(len(hedgehog)):
            hx, hy = hedgehog.popleft()
            for i in range(4):
                nhx = hx + dx[i]
                nhy = hy + dy[i]
                if 0 <= nhx < R and 0 <= nhy < C:
                    if graph[nhx][nhy] == "D":
                        return True
                    elif (graph[nhx][nhy] == "."):
                        graph[nhx][nhy] = "S"
                        hedgehog.append((nhx,nhy))
        
        for i in range(len(water)):
            wx, wy = water.popleft()

            for j in range(4):
                nwx = wx + dx[j]
                nwy = wy + dy[j]
                if 0 <= nwx < R and 0 <= nwy < C:
                        if (graph[nwx][nwy] == "." or graph[nwx][nwy] == "S"):
                            graph[nwx][nwy] = "*"
                            water.append((nwx,nwy))
                            if (nwx,nwy) in hedgehog:
                                hedgehog.remove((nwx,nwy))
        cnt+=1
    return False
        

for i in range(R):
    for j in range(C):
        if graph[i][j] == "D": #비버굴
            end_point = (i,j)
        elif graph[i][j] == "S": #고슴도치 위치
            hedgehog.append((i,j))
        elif graph[i][j] == "*": #물위치 
            water.append((i,j))

print(cnt+1 if bfs() else "KAKTUS")
