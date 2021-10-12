
import sys
from collections import deque
sys.stdin = open("input.txt",'rt')


N= int(input())
A = list(map(int,input().split()))

rocks = [1]*N 
MaxRocks = -1

for i in range(N):
    temp = []
    for j in range(N):
        if j < i and A[j] < A[i]:
            temp.append(rocks[j])
    if len(temp)!=0:
        rocks[i] = max(temp) + 1


print(max(rocks))

