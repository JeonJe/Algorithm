import sys
T = int(input())

for i in range(T):
    arr = list(map(str, sys.stdin.readline()))
    sum = 0
    cur_val = 0
    for j in arr:
        if j == 'O':
            cur_val+=1
            sum+=cur_val
        else:
            cur_val = 0
        
    print(sum)
