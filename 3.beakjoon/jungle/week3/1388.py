# from collections import deque
# #세로 N, 가로 M
# N, M = map(int,input().split())

# move= [-1,1]

# graph = [ list(input()) for _ in range(N) ]
# visited = [ [False]*M for _ in range(N) ]
# global cnt 
# cnt = 0

# def bfs(x,y):
#     que = deque()
#     que.append((x,y))
#     pattern = graph[x][y]
#     visited[x][y] = True

#     while que:
#         cx, cy = que.popleft()
       
#         for i in range(2):
#             if pattern == '-':
#                 nx = cx 
#                 ny = cy + move[i]
#             elif pattern == '|':
#                 nx = cx + move[i]
#                 ny = cy 
#             if 0 <= nx < N and 0 <= ny < M:
#                 if not visited[nx][ny] and graph[nx][ny] == pattern:
#                     visited[nx][ny] = True
#                     que.append((nx,ny))


# for i in range(N):
#     for j in range(M):
#         if not visited[i][j]:
#             cnt += 1
#             bfs(i,j)
# print(cnt)

print(bin(18))