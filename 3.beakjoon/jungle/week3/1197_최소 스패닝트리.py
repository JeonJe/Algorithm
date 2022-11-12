
v, e = map(int,input().split())

def find(parent, x):
    if parent[x] == x:
        return x

    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y ):
    rootX = find(parent, x)
    rootY = find(parent, y)
    
    if rootX < rootY:
        parent[rootY] = rootX
    else:
        parent[rootX] = rootY

graph = []
parent = [i for i in range(v+1)]
result = 0

for i in range(e):
    fr, to, weight = map(int,input().split())
    graph.append((weight,fr,to))

graph.sort()

for edge in graph:
    weight,fr,to = edge

    if find(parent, fr) != find(parent, to):
        union(parent,fr,to)
        result+=weight
print(result)