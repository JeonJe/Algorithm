from collections import deque 
import heapq

def solution(operations):
    answer = []
    que = []
    
    for oper in operations:
        operation, value = oper.split()
        value = int(value)
        
        if operation == "I":
            que.append(value)
        else:
            if que and value == 1 :
                heapq._heapify_max(que)
                heapq._heappop_max(que) 
            elif que and value == -1:
                heapq.heapify(que)
                heapq.heappop(que)
        
    if not que:
        return 0,0
    else:
        return [max(que), min(que)]
                
            