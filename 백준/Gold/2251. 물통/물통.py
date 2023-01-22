from collections import deque

A,B,C = map(int,input().split())

def bfs():

    def move_water(x,y):
        if not visited[x][y]:
            visited[x][y] = True
            que.append((x,y))
        
    que = deque()
    que.append((0,0))

    while que:
        # x : A에 남아있는 물의 양
        # y : B에 남아있는 물의 양
        x, y = que.popleft()

        # z : C에 남아있는 물의 양
        z = C - x - y 

        if x == 0:
            res.append(z)
        
        # A -> B
        move = min(x, B-y)
        move_water(x-move, y+move)
        # A -> C
        move = min(x, C-z)
        move_water(x-move, y)
        # B -> A
        move = min(y, A-x)
        move_water(x+move, y-move)
        # B -> C
        move = min(y, C-z)
        move_water(x, y-move)
        # C -> A
        move = min(z, A-x)
        move_water(x+move, y)
        # C -> B
        move = min(z, B-y)
        move_water(x, y+move)
        

visited = [[False]*(B+1) for _ in range(A+1)]
visited[0][0] = True
res = []

bfs()
res.sort()
print(*res)

