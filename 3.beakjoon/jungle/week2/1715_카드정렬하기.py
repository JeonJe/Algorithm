import heapq

n = int(input())
arr = [ int(input()) for _ in range(n)]
arr.sort()

min_heap = []
card_sum = 0

if len(arr) == 1:
    print(0)
    exit()

for a in arr:
    heapq.heappush(min_heap,a)

while len(min_heap) > 0:
    f = heapq.heappop(min_heap)
    if len(min_heap) == 1:
        card_sum += f + min_heap[0]
        break
    else:
        s = heapq.heappop(min_heap)
        card_sum += f+s
        heapq.heappush(min_heap,(f+s))

print(card_sum)