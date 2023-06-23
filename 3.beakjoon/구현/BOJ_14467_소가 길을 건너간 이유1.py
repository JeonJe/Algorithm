n = int(input())

seq = [list(map(int,input().split())) for _ in range(n)]
cows = [-1]*(n+1)

answer = 0

for cow_idx, point in seq:

    if cows[cow_idx] == -1:
        cows[cow_idx] = point
    
    else:
        if cows[cow_idx] != point:
            answer += 1
            cows[cow_idx] = point
print(answer)