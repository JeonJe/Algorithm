from collections import deque

def solution(food):
    left = deque()
    right = deque()
    
    foods = ""
    for i in range(len(food)):
        foods += str(i) * int(food[i])

    que = deque(foods)
    
    while len(que) > 0:
        if len(que) >= 2:
            if que[0] != que[1]:
                que.popleft()
                continue
            f = que.popleft()
            s = que.popleft()
            if f == s:
                left.append(f)
                right.append(s)
        else:
            que.popleft()
    
    right = list(reversed(right))
    answer = ''.join(left)+'0'+''.join(right)
        
    return answer