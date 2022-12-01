n = int(input())

meetings = [ list(map(int,input().split())) for _ in range(n) ]
meetings.sort(key=lambda x : (x[1],x[0]))

cnt = 0
prev_end = 0

for m in meetings:
    start , end = m[0], m[1]

    if prev_end <= start:
        cnt+=1
        prev_end = end 

print(cnt)