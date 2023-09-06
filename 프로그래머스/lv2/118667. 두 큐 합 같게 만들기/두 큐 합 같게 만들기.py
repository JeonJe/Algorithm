from collections import deque 

def solution(queue1, queue2):
    
    deque1 = deque(queue1)    
    deque2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    for i in range(4*len(queue1)):
        if sum1 > sum2:
            x = deque1.popleft()
            sum1 -= x
            sum2 += x
            deque2.append(x)
        elif sum1 < sum2:
            x = deque2.popleft()
            sum1 += x
            sum2 -= x
            deque1.append(x)
        else:
            return i 
            
    return -1