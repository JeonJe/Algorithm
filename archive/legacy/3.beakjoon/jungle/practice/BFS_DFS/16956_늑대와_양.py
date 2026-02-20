R, C = map(int,input().split())

graph = [list(input()) for _ in range(R)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

find_goat = False
for i in range(R):
    for j in range(C):
        if graph[i][j] == "W":
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if  0 <= nx < R and 0 <= ny < C:
                    if graph[nx][ny] == "S":
                        find_goat = True
                    elif graph[nx][ny] == ".":
                        graph[nx][ny] = "D"

if find_goat:
    print(0)
else:
    print(1)
    for i in range(R):
        print(''.join(graph[i]))

