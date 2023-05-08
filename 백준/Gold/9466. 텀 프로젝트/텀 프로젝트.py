import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline 

t = int(input())

def dfs(cur):
    global cnt 
    visited[cur] = True
    cur_want = pick[cur]

    if not visited[cur_want]:
        dfs(cur_want)
    else:
        if cur_want not in checked_member:
            nex = cur_want
            while nex != cur:
                cnt+=1
                nex = pick[nex]
            cnt+=1
    checked_member.add(cur)
    return 




for _ in range(t):
    n = int(input())
    pick = [0]+list(map(int,input().split()))

    visited = [False for _ in range(n+1)]
    checked_member = set()
    cnt = 0
    
    for i in range(1,n+1):
        if not visited[i]:
            dfs(i)
    print(n - cnt)