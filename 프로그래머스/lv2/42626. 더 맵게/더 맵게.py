import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for s in scoville:
        heapq.heappush(heap,s)
    
    while heap[0] < K:
        if len(heap) < 2:
            return -1
        
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        new = first + (second * 2)
        answer += 1
        heapq.heappush(heap,new)
    return answer
        