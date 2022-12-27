import sys 
input = sys.stdin.readline

n = int(input())
graph = [ list(map(int, input().split())) for _ in range(n) ]
distance = [[sys.maxsize] * (n) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            graph[i][j] = sys.maxsize

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


for i in range(n):
    for j in range(n):
        if graph[i][j] < sys.maxsize:
            print(1,end=' ')
        else:
            print(0,end=' ')
    print()       