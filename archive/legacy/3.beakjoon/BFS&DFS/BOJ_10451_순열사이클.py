t = int(input())

def dfs(cur):
    global cnt 

    visited[cur] = True
    next = seq[cur]
    cycle_list.append(cur)
    
    if not visited[next]:
        dfs(next)
    else:
        if next in cycle_list:
            cnt+=1
        return 
    


for _ in range(t):
    n = int(input())
    seq = [0] + list(map(int,input().split()))
    visited = [False] * (n+1)
    
    global cnt
    cnt = 0
    for i in range(1,n+1):
        if not visited[i]:
            cycle_list = []
            dfs(i)
    print(cnt)