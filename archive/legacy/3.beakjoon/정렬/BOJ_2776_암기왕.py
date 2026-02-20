from collections import defaultdict 
import sys 
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    n = int(input())
    dict = defaultdict(int)
    arr1 = list(map(int,input().split()))
    for i in arr1:
        dict[i] += 1


    M = int(input())
    arr2 = list(map(int,input().split()))
    for j in arr2:
        if dict[j] == 0:
            print(0)
        else:
            print(1)


