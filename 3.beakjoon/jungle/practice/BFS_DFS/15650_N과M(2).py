N,M = map(int,input().split())

arr = [ i for i in range(1, N+1)]

def dfs(depth, start, temp):
    if len(temp) == M:
        print(*temp)
        return
    
    if depth >= len(arr):
        return 
    
    for i in range(start, N+1):
        if temp[-1] < i:
            temp.append(i)
            dfs(depth+1, i, temp)
            temp.remove(i)

for i in range(1,N+1):
    dfs(0,i,[i])