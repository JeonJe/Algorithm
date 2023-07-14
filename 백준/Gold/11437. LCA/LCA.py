import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
LOG = 21

n = int(input())
graph = [ [] for i in range(n+1) ]

parent = [[0]* LOG for _ in range(n+1)]
node_depth = [0]*(n+1)
node_depth_calculated = [0]*(n+1)

for i in range(n-1):
    fr, to = map(int,input().split())
    graph[fr].append(to)
    graph[to].append(fr)

def dfs(x, depth):
    node_depth_calculated[x] = True
    node_depth[x] = depth 

    for adj in graph[x]:
        if not node_depth_calculated[adj]:
            # adj 노드의 2^0번째 조상은 x
            parent[adj][0] = x
            dfs(adj, depth+1)

def set_parent():
    #루트부터 depth 
    dfs(1,0)

    #2^i 번째 부모가 몇번 노드인지 계산
    for i in range(1, LOG):
        #j번째 노드 
        for j in range(1,n + 1):
            # j번째 노드의 2^i번째 부모 노드는 "j번째 노드의 i-1 부모 노드"의 i-1번째 부모
            parent[j][i] = parent[ parent[j][i-1] ][ i-1 ]
        
  
def lca(a, b):
    if node_depth[a] > node_depth[b]:
        a,b = b,a
    
    for i in range(LOG-1, -1, -1):
        if node_depth[b] - node_depth[a] >= (2**i):
            b = parent[b][i]

    if a == b:
        return a
    
    for i in range(LOG-1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    #공통조상 리턴 
    return parent[a][0]
    
set_parent()

m = int(input())

for i in range(m):
    a, b= map(int,input().split())
    print(lca(a, b))