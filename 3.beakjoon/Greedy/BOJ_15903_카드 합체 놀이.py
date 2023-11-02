import heapq 

n, m = map(int,input().split())
seq = list(map(int,input().split()))
heap = []

for num in seq:
    heapq.heappush(heap, num)
    
for i in range(m):
    f = heapq.heappop(heap)
    s = heapq.heappop(heap)

    temp = f+s
    heapq.heappush(heap, temp)
    heapq.heappush(heap, temp)

answer = 0

while heap:
    answer += heapq.heappop(heap)
print(answer)

