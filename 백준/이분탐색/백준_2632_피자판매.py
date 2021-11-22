
import sys
from collections import defaultdict


# sys.stdin = open("input.txt",'rt')

n,m = map(int,input().split())
arr = [ int(input()) for _ in range(m)]

left = 1
#한명이 다 가져간 경우
right = max(arr)


while left<=right:
    mid = (left+right)//2
    #보석을 m명보다 많이 나눌 수 있으면
    #보석을 더 작게 나눌 수 있음
    s = 0
    for i in arr:
        
        if i % mid == 0:
            s += i//mid
        else:
            s += (i//mid)+1

        #묶음수가 가져갈 사람보다 더 많으면
    if s > n:
        #left를 mid보다 크게함 -> 다음 i//mid 인 s값은 더 작아지고 다시 체크 
        left = mid+1
    else:
        right = mid-1

print(left)