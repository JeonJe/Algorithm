<<<<<<< HEAD
N,M = map(int,input().split())

arr = []
for _ in range (N):
    arr.append(list(map(int,input())))


def dfs(x,y):
    # map을 벗어나는 경우
    if x < 0 or x >= N or y < 0 or y >= M:
        return False

    if arr[x][y] == 0: #구멍이 뚫려있으면
        arr[x][y] = 1 #그래프 방문 처리
        dfs(x + 1, y) #아래
        dfs(x - 1, y) #위
        dfs(x , y + 1) # 오른쪽
        dfs(x , y - 1) #왼쪽
        return True

    return False # 뚫려있는 구멍이 없으면 False 리턴

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            result+=1

print(result)
=======
N,M = map(int,input().split())

arr = []
for _ in range (N):
    arr.append(list(map(int,input())))


def dfs(x,y):
    # map을 벗어나는 경우
    if x < 0 or x >= N or y < 0 or y >= M:
        return False

    if arr[x][y] == 0: #구멍이 뚫려있으면
        arr[x][y] = 1 #그래프 방문 처리
        dfs(x + 1, y) #아래
        dfs(x - 1, y) #위
        dfs(x , y + 1) # 오른쪽
        dfs(x , y - 1) #왼쪽
        return True

    return False # 뚫려있는 구멍이 없으면 False 리턴

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            result+=1

print(result)
>>>>>>> 65f2ee7131e2912c03d2122a15fcc235b3105750
