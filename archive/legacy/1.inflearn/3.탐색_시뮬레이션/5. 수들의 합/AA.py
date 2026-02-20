import sys

# sys.stdin = open("input.txt",'rt')

n,m = map(int,input().split())
arr = list(map(int,input().split()))

lt, rt = 0,1
tot = arr[0]
cnt=0


while True:
    if tot < m:
        if rt >= n:
            break
        else:
            tot += arr[rt]
            rt +=1
    elif tot == m:
        cnt+=1
        tot -= arr[lt]
        lt+=1

    else:
        tot -= arr[lt]
        lt+=1

print(cnt)