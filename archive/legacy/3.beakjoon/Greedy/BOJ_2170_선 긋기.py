n = int(input())
seq = [list(map(int,input().split())) for i in range(n)]

seq.sort()

prev_end = -1e9
answer = 0
for start,end in seq:
    #선분이 겹치지 않는 경우 
    if start >= prev_end:
        answer += end - start
        prev_end = end    
    #선분이 겹치는 경우 
    elif end > prev_end:
        answer += end - prev_end
        prev_end = end
        
print(answer) 