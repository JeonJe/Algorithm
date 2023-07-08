import heapq 

n = int(input())
drinks = list(map(int,input().split()))

heap = []
for d in drinks:
    heapq.heappush(heap, -d)

while len(heap) >= 2:
    f = heapq.heappop(heap) * -1
    s = heapq.heappop(heap) * -1
    mixed = (s / 2) + f
    heapq.heappush(heap, -mixed)


print(f'{heapq.heappop(heap) * -1}')
