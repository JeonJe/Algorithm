import sys

input = sys.stdin.readline 
n = int(input())

global graph, answer
graph = [ list(map(int,input().split())) for _ in range(n) ]
visited = [ False for _ in range(n)]
answer  = 1e9

def calculate_point():
    global graph, answer
    sum_team_a, sum_team_b = 0,0

    for i in range(n-1):
        for j in range(i+1,n):
            if visited[i] and visited[j]:
                sum_team_a += graph[i][j] + graph[j][i]
            elif not visited[i] and not visited[j]:
                sum_team_b += graph[i][j] + graph[j][i]

    answer = min(answer, abs(sum_team_a - sum_team_b))
    return 

def dfs(depth, index):
    if depth >= (n//2):
        calculate_point()
        return 
    
    for i in range(index, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)    
            visited[i] = False

dfs(0,0)
print(answer)