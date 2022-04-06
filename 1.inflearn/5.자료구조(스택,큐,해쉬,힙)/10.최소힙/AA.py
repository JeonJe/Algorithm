import sys
import heapq

# sys.stdin = open("input.txt",'rt')  

heap= []

while True:
    cur = int(input())

    if cur == -1:
        break

    elif cur == 0:
        if len(heap) == 0:
            print("-1")
        else:
            print(heapq.heappop(heap))
    
    else:
        heapq.heappush(heap,cur)