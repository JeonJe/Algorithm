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
                    if cur % oper[i] == 0:
                        que.append((cur / oper[i], cnt+1))
                else:
                    que.append((cur - oper[i], cnt+1))
        return -1    
        
    oper = [3,2,n]    
    if x == y:
        return 0 
    
    return bfs()
    