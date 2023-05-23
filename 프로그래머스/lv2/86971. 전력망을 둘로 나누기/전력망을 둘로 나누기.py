from collections import deque 
import copy

def bfs(x,graph,visited):
    cnt = 1
    visited[x] = True
    que = deque()
    que.append((x))
    
    while que:
        cx = que.popleft()

        for adj in graph[cx]:
            if not visited[adj]:
                visited[adj] = True
                que.append(adj)
                cnt+=1
    return cnt 


def find_min_diff(copy_graph, n):
    visited = [False for _ in range(n+1)]
    nums = []
    for i in range(1,n+1):
        if not visited[i]:
            nums.append(bfs(i,copy_graph,visited))
    return nums

def solution(n, wires):
    answer = n
    graph = [ [] for _ in range(n+1) ]
    #그래프 생성
    for fr, to in wires:
        graph[fr].append(to)
        graph[to].append(fr)

    #원복에서 그래프를 복사해와서 한군데씩 차례대로 짤라보기
    for i in range(1,n+1):
        for idx in graph[i]:
            copy_graph = copy.deepcopy(graph)
            copy_graph[i].remove(idx)
            result = find_min_diff(copy_graph,n)
            if len(result) == 2:
                answer = min(answer, abs(result[0] - result[1]))

    return answer