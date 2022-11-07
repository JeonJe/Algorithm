import sys
import heapq

n = int(sys.stdin.readline())
max_heap = []

for _ in range(n):
    n = int(sys.stdin.readline())
    if n == 0:
        if len(max_heap) > 0:
            print(heapq.heappop(max_heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(max_heap,(-n,n))
    