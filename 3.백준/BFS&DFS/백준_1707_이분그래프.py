
import sys
from collections import deque
input = sys.stdin.readline
# sys.stdin = open("input.txt",'rt')

def BFS(x):
    visited[x] = 1
    q = deque()
    q.append(x)

    while q:
        current = q.popleft()
        for i in graph[current]:
            if visited[i] == 0:
                visited[i] = -visited[current] #인접한 노드를 방문한적이 없다면 이전 노드의 반대로 표시 
                q.append(i)
            else:
                if visited[i] == visited[current]: #인접한 노드가 같은색이면 이분그래프가 아님
                    return False
    return True


K= int(input()) #테스트 케이스의 개수 

for i in range(K):
    v,e = map(int,input().split()) # 그래프의 정점의 개수 V와 간선의 개수 
    graph = [ [] for _ in range(v+1)]
    visited = [0]*(v+1)
    flag = 1

    for j in range(e):
      u,v = map(int,input().split()) # E개의 줄에 걸쳐 간선에 대한 정보
      graph[u].append(v)
      graph[v].append(u)
    for k in range(1,v+1):
        if visited[k] == 0:
            if not BFS(k):
                flag = -1
                break 
    print('YES' if flag==1 else 'NO') # 이분 그래프이면 YES,아니면 NO

