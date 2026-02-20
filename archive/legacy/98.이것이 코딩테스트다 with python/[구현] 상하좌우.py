<<<<<<< HEAD
N = int(input())

command = list(input().split())

arr = []

for _ in range(N):
    arr.append([0]*N)

x=1
y=1
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']
for com in command:
    for i in range(len(move_types)):
        if com == move_types[i]: # 다음 위치
            ny = y+dy[i]
            nx = x+dx[i]

    if nx > N or nx < 1 or ny > N or ny < 1: #다음 위치가 판 밖으로 나가면 이동 안함
        continue

    x ,y =  nx,ny # x,y 를 nx,ny 로 이동

=======
N = int(input())

command = list(input().split())

arr = []

for _ in range(N):
    arr.append([0]*N)

x=1
y=1
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']
for com in command:
    for i in range(len(move_types)):
        if com == move_types[i]: # 다음 위치
            ny = y+dy[i]
            nx = x+dx[i]

    if nx > N or nx < 1 or ny > N or ny < 1: #다음 위치가 판 밖으로 나가면 이동 안함
        continue

    x ,y =  nx,ny # x,y 를 nx,ny 로 이동

>>>>>>> 65f2ee7131e2912c03d2122a15fcc235b3105750
print(x,y)