import sys
from collections import deque
input = sys.stdin.readline
# R행 C열
# 비어있는 곳 . / 물이차있는 곳 * / 돌 X
# 비버 D / 고슴도치 S/
# 물이 매분마다 확장
R,C = map(int,input().split())
l =[[i for i in input().strip()]for _ in range(R)]
memo=[[sys.maxsize for _ in range(C)]for i in range(R)]
dx = [1,0,-1,0]
dy = [0,-1,0,1]
water = deque()
q =deque()
def check(a,b):
    if a<0 or b<0 or a>=R or b>=C: return False
    else: return True
def checkWater():
    waters = len(water)
    for _ in range(waters):
        a,b = water.popleft()
        for i in range(4):
            ax = a+dx[i]
            by = b+dy[i]
            if check(ax,by):
                if l[ax][by] == '.'or l[ax][by]=='S':
                    l[ax][by] = '*'
                    water.append((ax,by))
def checkHome():
    length = len(q)
    for _ in range(length):
        x,y = q.popleft()
        for i in range(4):
            xx= x+dx[i]
            yy= y+dy[i]
            if check(xx,yy) and memo[xx][yy] > memo[x][y]:
                if l[xx][yy] == '.':
                    memo[xx][yy] = memo[x][y] + 1
                    q.append((xx,yy))
                elif l[xx][yy] == 'D':
                    print(memo[x][y]+1)
                    exit(0)
def BFS(start):
    memo[start[0]][start[1]] = 0
    q.append(start)
    while q:
        checkWater()
        checkHome()
        
for i in range(R):
    for j in range(C):
        if l[i][j] =='*':
            memo[i][j] = 0
            water.append((i,j))
        elif l[i][j] == 'S':
            memo[i][j] = 0
            start = (i,j)
        elif l[i][j] == 'X':
            memo[i][j] = 0


BFS(start)
print('KAKTUS')