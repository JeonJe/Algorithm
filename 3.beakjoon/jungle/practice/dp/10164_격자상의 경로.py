

# N,M,K = map(int,input().split())

# graph = [[0]*M for _ in range(N)]
# dp = [ [[0 for _ in range(2)] for _ in range(M)] for _ in range(N) ]

# if K != 0:
#     circle_x = (K-1) // M
#     circle_y = (K-1) % M
#     graph[circle_x][circle_y] = 1

# dx = [0,1]
# dy = [1,0]

# # for i in range(N):
# #     for j in range(M):
# #         print(dp[i][j],end=' ')
# #     print()
# for i in range(N):
#     for j in range(M):
#         if (i == 0 and j == 0) or (i == N-1 and j == M-1):
#             continue    
#         if graph[i][j] == 1:
#             dp[1]
#         else