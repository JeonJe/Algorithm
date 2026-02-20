from collections import deque 
import copy 


def topology_sort():
    res = copy.deepcopy(time)

    while que:
        cv = que.popleft()

        for adj in graph[cv]:
            indegree[adj] -= 1
            res[adj] = max(res[adj], res[cv]+time[adj])

            if indegree[adj] == 0:
                que.append(adj)
    
    for i in res:
        if i != 0:
            print(i)

N = int(input())
graph = [ [] for _ in range(N+1) ]
indegree = [0] *(N+1)
time = [0] * (N+1)

for i in range(1,N+1):
    data = list(map(int,input().split()))
    time[i] = data[0]

    for v in data[1:-1]:
        indegree[i] += 1


        graph[v].append(i)

que = deque()

#간선의 수가 0인 부분부터 큐에 넣기 
for i in range(1,len(indegree)):
    if indegree[i] == 0:
        que.append(i)

topology_sort()