import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline 

t = int(input())

def dfs(cur):
    global cnt 
    visited[cur] = True
    cycle_list.append(cur)
    cur_want = pick[cur]
    
    if not visited[cur_want]:
        dfs(cur_want)
    else:
        if cur_want in cycle_list:
            cnt += len(cycle_list[cycle_list.index(cur_want) : ])    
        return 


for _ in range(t):
    n = int(input())
    pick = [0]+list(map(int,input().split()))

    visited = [False] *(n+1)
    cnt = 0

    for i in range(1,n+1):
        if not visited[i]:
            cycle_list = []
            dfs(i)
    print(n - cnt)
