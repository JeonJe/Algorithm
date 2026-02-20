
import sys
sys.stdin = open("input.txt",'rt')

N = int(input())


arr = [input() for _ in range(N)]
arr2 = [input() for _ in range(N-1)]

arr.sort()
arr2.sort()

for i in range(N-1):
    if arr[i] != arr2[i]:
        break

else:
    print(arr[N])