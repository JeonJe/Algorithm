import sys 
sys.setrecursionlimit(10**9)
def solution(x, y, n):    
    def dfs(target, cur, cnt):
        global answer

        if cur > target or cnt > answer:
            return

        if cur == target:
            answer = min(answer,cnt)
            return 
        
        for i in [3,2,n]:
            if i == n:
                dfs(target,cur+i,cnt+1)
            else:
                dfs(target,cur*i,cnt+1)

    global answer
    answer = 333334
    dfs(y,x,0)
    if answer == 333334:
        return -1
    else:
        return answer





x = 1
y = 1 
n = 4

print(solution(x,y,n))