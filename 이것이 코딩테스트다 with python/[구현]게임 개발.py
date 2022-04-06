<<<<<<< HEAD
N , M = map(int,input().split())
row, col, direction = map(int,input().split())

#방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
visited= [[0]*M for _ in range(N)]

#현재 좌표 방문처리
visited[row][col] = 1

arr = []
for _ in range(M):
    arr.append(list(map(int,input().split())))

#북,동,남,서 이동

drow = [-1,0,+1,0]
dcol = [0,+1,0,-1]

def turn_left():
    global direction
    direction -=1
    if direction < 0:
        direction = 3


#시뮬레이션 시작
count = 1
#네 방향 모두 움직일 수 없을 경우를 확인하기 위한 변수 turn_time
turn_time = 0

while True:
 #왼쪽방향 회전
    turn_left()

#다음 row,col 은 현재 좌표 + 방향으로 한칸 전진
    nrow = row + drow[direction]
    ncol = col + dcol[direction]
 #회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if arr[nrow][ncol] ==0 and visited[nrow][ncol] ==0:
# 방문 표시
        visited[nrow][ncol]=1
# 방문 칸 카운트
        count+=1
        turn_time =0
# 좌표 이동
        row,col =nrow,ncol
        continue

#회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time+=1

#네 방향 모두 갈 수 없는 경우
    if turn_time ==4:
 #한 칸 뒤로 후진
        ncol = col - dcol[direction]
        nrow = row - drow[direction]
        if arr[nrow][ncol] == 0:
            col = ncol
            row = nrow
        else:
            break
        turn_time = 0
print(count)


=======
N , M = map(int,input().split())
row, col, direction = map(int,input().split())

#방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
visited= [[0]*M for _ in range(N)]

#현재 좌표 방문처리
visited[row][col] = 1

arr = []
for _ in range(M):
    arr.append(list(map(int,input().split())))

#북,동,남,서 이동

drow = [-1,0,+1,0]
dcol = [0,+1,0,-1]

def turn_left():
    global direction
    direction -=1
    if direction < 0:
        direction = 3


#시뮬레이션 시작
count = 1
#네 방향 모두 움직일 수 없을 경우를 확인하기 위한 변수 turn_time
turn_time = 0

while True:
 #왼쪽방향 회전
    turn_left()

#다음 row,col 은 현재 좌표 + 방향으로 한칸 전진
    nrow = row + drow[direction]
    ncol = col + dcol[direction]
 #회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if arr[nrow][ncol] ==0 and visited[nrow][ncol] ==0:
# 방문 표시
        visited[nrow][ncol]=1
# 방문 칸 카운트
        count+=1
        turn_time =0
# 좌표 이동
        row,col =nrow,ncol
        continue

#회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time+=1

#네 방향 모두 갈 수 없는 경우
    if turn_time ==4:
 #한 칸 뒤로 후진
        ncol = col - dcol[direction]
        nrow = row - drow[direction]
        if arr[nrow][ncol] == 0:
            col = ncol
            row = nrow
        else:
            break
        turn_time = 0
print(count)


>>>>>>> 65f2ee7131e2912c03d2122a15fcc235b3105750
