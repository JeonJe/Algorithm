from collections import deque

def bfs(start):
    start_x, start_y = start
    que = deque()
    que.append((start_x, start_y))
    visited = [ False for _ in range(n) ]
    result  = "sad"
    while que:
        cx, cy = que.popleft()

        if abs(cx - desti[0]) + abs(cy - desti[1]) <= 1000:
            result = "happy"
            break

        for i in range(n):
            distance_to_store = abs(cx - store[i][0]) + abs(cy-store[i][1])
            if not visited[i] and distance_to_store <= 1000:
                visited[i] = True 
                que.append((store[i][0], store[i][1]))

    return result


t = int(input())

for _ in range(t):
    n = int(input())
    home = list(map(int,input().split()))
    store = [list(map(int,input().split())) for _ in range(n)]
    desti = list(map(int,input().split()))

    print(bfs(home))
    
               