from collections import deque
n = int(input())
seq = input()

def find(parent, x):
    if x == parent[x]:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    rootX = parent[x]
    rootY = parent[y]

    if rootX == rootY:
        return 
    
    if rootX < rootY:
        parent[y] = rootX
    else:
        parent[x] = rootY
        

parent = [ i for i in range(n)]
visited = [False] * (n)

for i in range(n):
    if seq[i] == "E":
        union(parent, i, i+1)
    else:
        union(parent, i, i-1)


print(len(set(parent)))