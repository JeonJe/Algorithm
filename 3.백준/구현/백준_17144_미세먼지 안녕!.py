import sys


def dust_spread():
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    temp_arr = [ [0]*C for _ in range(R) ]

    for i in range(R):
        for j in range(C):
            if arr[i][j] >0 :
                temp = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0<=nx<R and 0<=ny<C and arr[nx][ny] != -1:
                        temp_arr[nx][ny] += arr[i][j] // 5
                        temp += arr[i][j] // 5
                arr[i][j] -= temp

    for i in range(R):
        for j in range(C):
            arr[i][j] += temp_arr[i][j]

def upper_aircon():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    x = up
    y = 1
    direction = 0
    before = 0

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        #위쪽 공기청정기가 처음 위치로 왔으면 반복문 종료
        if x == up and y == 0 :
            break
        #한쪽 방향으로 모두 이동하였다면 방향 전환
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direction+=1
            continue
        #처음은 공기청정기 바로 오른쪽 칸이고 값은 0 ( 공기청저기가 미세먼지 0으로 만듬)
        #그다음은 up,1 부터 값을 direction 방향으로 옮김
        arr[x][y],before =  before,arr[x][y]

        x = nx
        y = ny

def lower_aircon():
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]

    x = down
    y = 1
    direction,before = 0,0

    while True:
        nx = x+dx[direction]
        ny = y+dy[direction]

        if x == down and y == 0:
            break
        if nx < 0 or nx >=R or ny < 0 or ny >= C:
            direction+=1
            continue

        arr[x][y],before = before,arr[x][y]
        x = nx
        y = ny

if __name__ == "__main__":

    input = sys.stdin.readline
    R, C, T = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(R)]
    up,down = -1,-1

    for i in range(R):
        if arr[i][0] == -1:
            up = i
            down = i + 1
            break

    for t in range(T):
        dust_spread()
        upper_aircon()
        lower_aircon()

    ans = 0
    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0:
                ans+=arr[i][j]

    print(ans)
