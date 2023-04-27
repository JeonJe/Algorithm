# from collections import deque 

# n = int(input())
# graph = [list(input()) for _ in range(n)]

# dx = [-1,0,1,0]
# dy = [0,-1,0,1]

# def BFS(i,j,graph,visited):
#     cur_color = graph[i][j]
#     que = deque()
#     que.append((i,j))

#     while que:
#         cx,cy = que.popleft()

#         for i in range(4):
#             nx = cx + dx[i]
#             ny = cy + dy[i]

#             if 0 <= nx < n and 0 <= ny <n:
#                 if not visited[nx][ny] and graph[nx][ny] == cur_color:
#                     visited[nx][ny] = True
#                     que.append((nx,ny))
#     return 

# answer1 = 0
# visited = [ [False for _ in range(n)] for _ in range(n) ]
# for i in range(n):
#     for j in range(n):
#         if not visited[i][j]:
#             visited[i][j] = True 
#             BFS(i,j,graph,visited)
#             answer1+=1

# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == "G":
#             graph[i][j] = "R"

# answer2 = 0
# visited = [ [False for _ in range(n)] for _ in range(n) ]
# for i in range(n):
#     for j in range(n):
#         if not visited[i][j]:
#             visited[i][j] = True 
#             BFS(i,j,graph,visited)
#             answer2+=1

# print(answer1,answer2)

def solution(grid):
    answer = 0
    for i in range(4):
        for j in range(4):
            for k in range(j + 1, 4, 2):
                print(i,j,k )
                answer = max(answer, max(grid[i][j] + grid[j][k], grid[j][k] + grid[k][i]))
            print()
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니 위의 코드만 수정하세요.
grid = [[1, 4, 16, 1], [20, 5, 15, 8], [6, 13, 36, 14], [20, 7, 19, 15]]
ret = solution(grid)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")