n = int(input())

global cnt 
cnt = 0

#같은 행에 배치했는지 체크, True면 해당 열에 배치 됨 
flag_a = [False] * n 
#오른쪽 위 , 왼쪽 아래 방향 대각선으로 퀸을 배치 했는지 체크 
flag_b = [False] * (2*n-1)
flag_c = [False] * (2*n-1) 


# def queen(x):
#     global cnt
#     #y는 몇번쨰 행인지 나타냄 
#     for y in range(n):
#         #flag_b : 오른쪽 위 , 왼쪽 아래 대각선 확인 - j행 i열의 값은 i+j 
#         #flag_c : 왼쪽 위, 오른쪽 아래 대각선 확인 -  j행의 i열의 값은 i - j + (n-1)
#         if  not flag_a[y] and not flag_b[x+y] and not flag_c[x - y + (n-1) ]:
#             # pos[x] = y 
#             if x == (n-1):
#                 cnt+=1
#             else:
#                 flag_a[y] = flag_b[x+y] = flag_c[x-y+(n-1)] = True 
#                 queen(x + 1)
#                 flag_a[y] = flag_b[x+y] = flag_c[x-y+(n-1)] = False

# queen(0)
# print(cnt)

# n = int(input())

# ans = 0
# row = [-1] * n

# # row[x] (x행)에 퀸을 놓는 경우 유효성 검사
# def backtracking(x):
#     # 이전 행을 돌면서 놓인 퀸 위치 중 같은 행 또는 열, 대각선이 있는 지 검사
#     # 이전 행을 검사하는 이유? - 이전 행은 이미 유효한 위치이기 때문
#     for i in range(x):  
#         if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i): # 같은 col, 대각선 검사
#             return False
#     return True

# def n_queens(x):
#     global ans
#     if x == n: # n개의 퀸을 모두 놓았을 경우 ans++
#         ans += 1
#     else:
#         for i in range(n): # row check (열 순회)
#             row[x] = i
#             if backtracking(x): # 유효하면 다음 스텝으로 넘어감
#                 n_queens(x+1) # 다른 row 검사(행 순회)
# n_queens(0)
# print(ans)