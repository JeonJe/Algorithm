import sys 

N = int(input())
graph = [ list(map(int,input().split())) for _ in range(N) ]

global cnt
cnt = sys.maxsize 


def TPS(visited, cur_node , distance, init):
    global cnt 
    if False not in visited:
        if  graph[cur_node][init] != 0:
            cnt = min(cnt, distance + graph[cur_node][init])
            
    else:
        for next in range(N):
            if visited[next] or graph[cur_node][next] == 0:
                continue

            visited[next] = True
            TPS(visited, next, distance+graph[cur_node][next], init)
            visited[next] = False


for init_node in range(N):
    visited = [False] * (N)
    visited[init_node] = True 
    TPS(visited, init_node, 0, init_node)
   

print(cnt)
    

    


