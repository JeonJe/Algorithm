import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] == x:
        return parent[x]
    
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    rootX = parent[x]
    rootY = parent[y] 

    if rootX == rootY:
        return 
    
    if rootX < rootY:
        parent[rootX] = rootY
    else:
        parent[rootY] = rootX
    

t = int(input())

for case in range(1,t+1):
    # 유저 수
    n = int(input())
    
    #친구 관계 수 
    k = int(input())

    relation = [list(map(int,input().split())) for _ in range(k) ]

    #미리 구해야 할 쌍의 개수 
    m = int(input())

    seq = [ list(map(int,input().split())) for _ in range(m)]

    parent = [ i for i in range(n+1) ]
    graph = [ [] for i in range(n+1) ]

    for a,b in relation:
        if find(parent, a) != find(parent, b):
            union(parent, a, b)

    #각 노드에 대해 부모를 찾음 
    #seq의 두 부모가 같으면 1, 다르면 0 
    print(f'Scenario {case}:' )
    for a,b in seq:
        if find(parent, a) != find(parent, b):
            print(0)
        else:
            print(1)
    print()
    
