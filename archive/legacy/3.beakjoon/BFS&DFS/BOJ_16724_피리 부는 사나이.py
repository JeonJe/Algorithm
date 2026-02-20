height, width = map(int,input().split())

board = [list(input()) for _ in range(height)]

visited = [False] * (width*height)
parent = [ i for i in range(width * height)]

#남(D),동(R),북(U),서(L)
direct = {
    "D" : [1,0],
    "R" : [0,1],
    "U" : [-1,0],
    "L" : [0,-1]
}

def find(x, parent):
    if x == parent[x]:
        return parent[x]
    parent[x] = find(parent[x], parent)
    return parent[x]

def union(x, y, parent):
    root_x = find(x, parent)
    root_y = find(y, parent)

    if root_x == root_y:
        return False
    
    if root_x < root_y:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y
    return True

def dfs(x,y):
    
    cur = width * x + y
    visited[cur] = True

    dx,dy = direct[board[x][y]]
    nx = x + dx
    ny = y + dy
    next = width * nx + ny

    if not union(cur,next, parent) or visited[next]:
      return 
    else:
      dfs(nx, ny)

cnt = 0
for i in range(height):
    for j in range(width):
            dfs(i,j)
print(len(set(parent)))