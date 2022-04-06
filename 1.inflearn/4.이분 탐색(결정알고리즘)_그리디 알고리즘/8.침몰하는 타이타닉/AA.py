import sys

# sys.stdin = open("input.txt",'rt')


N, M = map(int,input().split())

arr = list(map(int,input().split()))
arr.sort()
left = 0
right = N-1
res = 0

while left <= right:
    if arr[left] + arr[right] <= M :

        left+=1
        right-=1
        res+=1
    else:

        right-=1
        res+=1

print(res)