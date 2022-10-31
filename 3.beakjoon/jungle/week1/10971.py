import sys 

N = int(input())
graph = [ list(map(int,input().split())) for _ in range(N) ]

global cnt
cnt = sys.maxsize 


def TPS(visited, cur_node , distance, init, depth):
    global cnt 
    if False not in visited:
        if depth == N and graph[cur_node][init] != 0:
            cnt = min(cnt, distance + graph[cur_node][init])
            #처음 찾았던 4가 1로 카운트됨 
    else:
        for next in range(N):
            if visited[next] or graph[cur_node][next] == 0:
                continue

            visited[next] = True
            TPS(visited, next, distance+graph[cur_node][next], init, depth+1)
            visited[next] = False


for init_node in range(N):
    visited = [False] * (N)
    visited[init_node] = True 
    TPS(visited, init_node, 0, init_node , 1)
   

print(cnt)
    

    


