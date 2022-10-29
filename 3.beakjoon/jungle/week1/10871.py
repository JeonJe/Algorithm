# 10 5
# 1 10 4 9 2 3 8 5 7 6
import sys 

N, X = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

for i in arr:
    if i < X:
        print(i, end=" ")