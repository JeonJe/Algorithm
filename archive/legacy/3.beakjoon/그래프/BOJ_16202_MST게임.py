
def union(parent,x,y):
    rootX = find(parent,x)
    rootY = find(parent,y)

    if rootX < rootY:
        parent[rootY] = rootX
    else:
        parent[rootX] = rootY

def find(parent,x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def kruskal(num_v,graph,parent):
    mst = 0
    edge_cnt = 0
    for weight, fr, to in graph:
        if find(parent,fr) != find(parent,to):
            union(parent,fr,to)
            mst += weight 
            edge_cnt += 1
    
    return mst if edge_cnt == num_v-1 else 0

#정점의 개수 N, 그래프 간선의 개수 M, 턴의 수 K
N,M,K = map(int,input().split())
graph = []
parent = [ i for i in range(N+1)]

for i in range(M):
    fr,to = map(int,input().split())
    weight = i+1
    graph.append((weight,fr,to))
graph.sort()

# 첫번째 턴
answer = []
answer.append(kruskal(N,graph,parent))

# 두 번째 턴과 그 이후 턴 
for _ in range(1,K):
    if len(graph) > 0:
        graph.pop(0)        
        parent = [ i for i in range(N+1)]
        answer.append(kruskal(N,graph,parent))

print(*answer)

