import sys 
import heapq

n = int(input())

min_heap = []
max_heap = []

f = int(input())
if n == 1:
    print(f)
    exit()
else:
    heapq.heappush(max_heap,(-f,f))
    print(f)

for i in range(1,n):
    f = int(sys.stdin.readline())
    if len(max_heap) > len(min_heap):
        heapq.heappush(min_heap, f)
    else:
        heapq.heappush(max_heap, (-f,f))
    
    if len(min_heap) > 0 and len(max_heap) > 0:
        min_top = min_heap[0]
        max_top = max_heap[0][1]

        if min_top < max_top:
            heapq.heappop(min_heap)
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, (-min_top, min_top))
            heapq.heappush(min_heap, max_top)
            
        print(max_heap[0][1])
        
        
    


