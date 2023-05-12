from collections import deque 

n = int(input())

seq = []
for i in range(n):
    sm,sd,em,ed = map(int,input().split())
    seq.append((sm*100 + sd, em*100 + ed))

seq.sort()
seq = deque(seq)
prev_end_date = 301
cnt = 0

while seq:

    cur_start_date = seq[0][0]
    if prev_end_date >= 1201 or cur_start_date > prev_end_date:
        break 
    
    temp = -1

    while seq:
        temp_start, temp_end = seq[0]
        #꽃이 피는 시작일이 prev_end_date 보다 작은 날짜 중 
        #꽃이 가장 늦게 지는 일을 찾아야 함
        if temp_start <= prev_end_date:
            temp = max(temp, temp_end)
            seq.popleft()
        else:   
            break
    #가장 늦게 지는 꽃의 날짜
    prev_end_date = temp
    cnt+=1

print(0 if prev_end_date < 1201 else cnt)
