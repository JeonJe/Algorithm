import sys

# sys.stdin = open("input.txt",'rt')


N = int(input())


arr = [list(map(int,input().split())) for _ in range(N)]

arr.sort(key=lambda x: (x[1]))
cnt=1
prev_start, prev_end = arr[0][0], arr[0][1]

for i in range(1,N):
    start,end = arr[i][0], arr[i][1]
    if start >= prev_end:

        prev_start = start
        prev_end = end
        cnt+=1
        

print(cnt)