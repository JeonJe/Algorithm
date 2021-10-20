

import copy
from collections import deque

import sys

input = lambda : sys.stdin.readline().strip()


# stdin = open("input.txt",'rt')

dx = [-1,0,1,0]
dy = [0,1,0,-1]



def count_zero(x,y):
    cnt = 0
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<=nx<N and 0<=ny<M and Map[nx][ny]==0:
            cnt+=1
    return cnt

    


def check_melt():
    for i in range(N):
        for j in range(M):
            if Map[i][j] != 0 :
                return False
    return True



def bfs(x,y):
    deq = deque()
    deq.append((x,y))
    visited = [ [0]* M for _ in range(N)]
    visited[x][y] = 1
    while deq:
        x,y = deq.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            #맵 안이면서, 방문한적 없고, 바다가 아닌 빙산인 곳 
            if 0<=nx<N and 0<=ny<M and visited[nx][ny]==0 and copy_map[nx][ny]!=0:
                visited[nx][ny] = 1
                copy_map[nx][ny] = 0
                deq.append((nx,ny))

#얼음이 모두 녹았는지 확인하고, 전체가 0 이면 0을 출력


N,M = map(int,input().split())
Map = [ list(map(int,input().split())) for _ in range(N)]
year = 0

while True:
    year +=1
    #빙산이 모두 다 녹았을 경우 
    if check_melt():
        print(0)
        break
    
    #원본 데이터로 빙산이 녹는 것을 계산 
    copy_map = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if Map[i][j] != 0 :

                number_of_zero = count_zero(i,j)
                nh = Map[i][j] - number_of_zero
                copy_map[i][j] = nh if nh >=0 else 0
    #원본 데이터 갱신
    Map = copy.deepcopy(copy_map)

    #빙산의 개수 확인 
    cnt = 0
    
    for i in range(N):
        for j in range(M):
            if copy_map[i][j] != 0:
                bfs(i,j)
                cnt+=1

    if cnt >= 2:
        print(year)
        break
