
import heapq 
import sys 
input = sys.stdin.readline
n = int(input())

que = []
for i in range(n):
    num = int(input())
    if num != 0:
        heapq.heappush(que, num)
    else:
        if que:
            print(heapq.heappop(que))
        else:
            print(0)

