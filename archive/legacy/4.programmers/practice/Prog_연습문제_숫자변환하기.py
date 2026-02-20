from collections import deque 
def solution(x, y, n):
    
    def bfs():    
        que = deque()
        que.append((y,0))
    
        while que:
            cur, cnt = que.popleft()
            if cur == x:
                return cnt
            if cur < x:
                continue

            for i in range(len(oper)):
                if i != 2:
                    que.append((cur / oper[i], cnt+1))
                else:
                    que.append((cur - oper[i], cnt+1))
        return -1    
        
    oper = [3,2,n]    
    if x == y:
        return 0 
    
    return bfs()
    


# x	y	n	result
# 10	40	5	2
# 10	40	30	1
# 2	5	4	-1

x = 2
y = 5
n = 4
print(solution(x,y,n))