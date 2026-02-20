import sys 
sys.setrecursionlimit(10**6)
def solution(n):
    def dfs(n):
        global cnt 
        if n == 0:
            return 
        if n % 2 == 0:
            dfs(n//2)
        else:
            cnt+=1
            dfs(n-1)


    global cnt 
    cnt = 0
    if n == 1 or n== 2:
        return 1
    dfs(n)
    return cnt

N = 5000

print(solution(N))