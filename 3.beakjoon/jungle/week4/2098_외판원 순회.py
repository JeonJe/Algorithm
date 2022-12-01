import sys
input = sys.stdin.readline
from collections import deque 

N = int(input())
graph = [ list(map(int,input().split())) for _ in range(N) ]
for i in range(N):
    for j in range(N):
        print(graph[i][j],end='  ')
    print()
print()
print()

for k in range(N):
    for a in range(N):
        for b in range(N):
            graph[a][b] =  min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(N):
    for j in range(N):
        print(graph[i][j],end='  ')
    print()