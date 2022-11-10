import sys
n = int(input())

circle_points = []


for _ in range(n):
    x, r = map(int,sys.stdin.readline().split())
    circle_left =  x - r
    circle_right = x + r
    circle_points.append((circle_left,'('))
    circle_points.append((circle_right, ')'))

#좌표 오름차순으로 정렬하고, 같은 좌표일 시 닫는 괄호가 ')' 먼저 오도록 정렬 
circle_points.sort(key = lambda x : (x[0], -ord(x[1])))
stack = []
cnt = 1

for i in range(n * 2):
    position, bracket = circle_points[i]

    if len(stack) == 0:
        stack.append({'pos':position,'bracket':bracket,'status':0})
        continue

#닫는 괄호 ')'가 들어 올시 
    if bracket == ')':
        #이전 원이 닫히지 않았을 경우 하나의 공간 추가
        if stack[-1]['status'] == 0:
            cnt += 1
        #이전 원과 원의 왼쪽 좌표에서 접점이 있음 공간이 2개로 분리
        elif stack[-1]['status'] == 1:
            cnt+=2
        #이전 원과 현재원이 닫혔으므로 stack에서 이전 원에 대한 정보 pop 
        stack.pop()
        #원이 이어져 있는지 확인
        #마지막 원의 좌표가 아닐  때 
        if i != n*2 - 1:
            #다음 원이 현재 원과 연결되어 있지 않으면, 이전 열린 원의 status는 0
            if circle_points[i+1][0] != position:
                stack[-1]['status'] = 0
#열린 괄호'(' 가 들어올 시 
#이전 원의 왼쪽 좌표와 비교하여 겹침 여부 확인 
    else:
        if stack[-1]['pos'] == position:
            #좌표가 같으면 원이 접해 있는 상태이므로 이전 원의 status는 1로 업데이트 후 현재 원 정보 push
            stack[-1]['status'] = 1
            stack.append({'pos':position,'bracket':bracket,'status':0})
        else:   
            # 좌표값이 같지 않으면 원이 접하지 않으므로 이전 원 갱신없이 현재원 정보 push
            stack.append({'pos':position,'bracket':bracket,'status':0})

print(cnt )