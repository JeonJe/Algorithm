import sys 
input = sys.stdin.readline
INF = sys.maxsize

def dfs(current, visited):
    #모든 노드를 방문 
    if visited == (1<<N) - 1:
        if graph[current][0] == 0: #출발점으로 가는 경로가 없을 때 
            return INF
        else:        #출발점으로 가는 경로가 있을 때 
            return graph[current][0]
    
    if dp[current][visited] != 0: #이미 최소비용이 계산되어 있다면 스킵 
        return dp[current][visited]
    
    temp=INF
    for i in range(N): #모든 도시를 탐방하면서, 방문한적이 없고, 현재노드와 이어져 있는 노드라면 최소값 확인
        if not (visited & (1<<i)) and graph[current][i] != 0:
            temp = min(temp, dfs(i, visited | (1<<i)) + graph[current][i])
    dp[current][visited] = temp
    return dp[current][visited]


N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
dp = [ [0]*(1<<N) for _ in range(N) ]

print(dfs(0,1))