import sys
import heapq
input = sys.stdin.readline

n = int(input())

left_max_heap = []
right_min_heap = []

for i in range(n):
    num = int(input())

    if len(right_min_heap) == len(left_max_heap):
        heapq.heappush(left_max_heap, num * -1)
    else:
        heapq.heappush(right_min_heap, num)

    if len(left_max_heap) > 0 and len(right_min_heap) > 0 and left_max_heap[0] * -1 > right_min_heap[0]:
        temp_max = heapq.heappop(left_max_heap) * -1
        temp_min = heapq.heappop(right_min_heap)
        heapq.heappush(right_min_heap, temp_max)
        heapq.heappush(left_max_heap, temp_min * -1)
    print(left_max_heap[0] * -1)
                                              