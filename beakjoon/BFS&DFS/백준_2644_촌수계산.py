
import sys
from collections import deque
# sys.stdin = open("input.txt",'rt')

def BFS(N):
    deq = deque()
    deq.append(N)

    while deq:
        current = deq.popleft()
        for x in graph[current]:
            if check[x]==0: #연결된 가족들을 확인, 확인하지 않은 가족이라면
                check[x] = check[current]+1
                deq.append(x)


n= int(input()) #전체 사람의 수 
s,e = list(map(int,input().split())) # 촌수를 계산해야 하는 서로 다른 두 사람의 번호 
m = int(input()) # 부모 자식들 간의 관계의 개수 m

temp=[]
graph = [ [] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,input().split())    
    graph[u].append(v)
    graph[v].append(u)

check = [0]*(n+1)
BFS(s)

print(check[e] if check[e] > 0 else -1)
