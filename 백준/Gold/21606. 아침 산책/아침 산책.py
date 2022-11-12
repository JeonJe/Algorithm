import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
in_out = list(map(int,input().rstrip()))
in_out.insert(0,-1)

graph = [ [] for _ in range(n+1) ]
global cnt 
cnt = 0


def bfs(v):
    global cnt
    
    que = deque()
    visited[v] = True
    que.append(v)
    num_in = 0
    while que:
        cur = que.popleft()
        for adj in graph[cur]:
            if not visited[adj]:
                #인접노드가 실외일 때 추가 bfs를 실행하여 인접한 실내 개수를 새야함 
                if in_out[adj] == 0:
                    visited[adj] = True
                    que.append(adj)
                else:
                    #실외 개수 추가
                    num_in +=1 
    return num_in

for _ in range(n-1):
    fr, to = map(int,input().split())
    graph[fr].append(to)
    graph[to].append(fr)
    #실내1 -> 실내 2, 실내2-> 실내1
    if in_out[fr] == in_out[to] == 1:
        cnt+=2
    

#각각의 노드에서 출발하는 것이 아니라 한번에 확인 후 개수를 구하느 것이기때문에
# visited는 for문 밖에서 한번만 실행
visited = [False] * (n+1)
for i in range(1,n+1):
    num_in = 0
    #실내이면 넘어가기
    if in_out[i] == 1:
        continue
    #방문하지 않은 실외에서 부터 도달할 수 있는 실내가 몇 개 있는지 확인 
    if not visited[i]:
        num_in = bfs(i)
    cnt += num_in * (num_in -1)
    
print(cnt)