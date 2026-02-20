N, M = map(int,input().split())
r,c,d = map(int,input().split())

#0 청소칸 -> 청소후 이동 x
#1 벽
graph = [ list(map(int,input().split())) for _ in range(N) ]
graph[r][c] = 2

#0북, 1동, 2남, 3서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

cnt = 1
def check_left(r,c,d):
    nr = r + dx[(d-1)%4]
    nc = c + dy[(d-1)%4]

    if graph[nr][nc] == 0:
        return True
    else:
        return False

def check_four(r,c,d):
    for i in range(1,5):
        nr = r + dx[(d-i)%4]
        nc = c + dy[(d-i)%4]
        if graph[nr][nc] == 0:
            return True
    return False

while True:
    #현재 바라보고 있는 방향의 왼쪽방향부터 차례대로 탐색
        #왼쪽 방향으로 갈 수 있으면? 이동 
    if check_left(r,c,d):
        r = r + dx[(d-1)%4]
        c = c + dy[(d-1)%4]
        graph[r][c] = 2
        cnt += 1
        d = (d-1)%4
        continue
    else:
        #네방향이 막히지 않았으면?
        #방향만 이동 
        if check_four(r,c,d):
            d = (d-1)%4
            continue
        else:
        #네방향이 막혔으면? 뒤에 벽인지 확인
            if graph[r + dx[(d+2)%4]][c + dy[(d+2)%4]] == 1:
                print(cnt)
                exit()
            else:
                #네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽방향으로 후진가능 한 경우
                r = r - dx[d]
                c = c - dy[d]