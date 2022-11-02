def dfs(cur_node,cnt,l):
    global res

    if False not in visited:
        sum = 0
  
        for i in range(n-1):
            sum += abs(l[i] - l[i+1])
        res = max(res,sum)
    else:
        for next_node in range(n):
            if visited[next_node] is False:
                visited[next_node] = True
                l[cnt] = arr[next_node]
                dfs(next_node,cnt+1,l)
                visited[next_node] = False
                
                

n = int(input())
arr =  list(map(int,input().split()))
global res 
global cnt
global l 

res = 0

for init_node in range(n):
    visited = [False]*(n)
    cnt = 0
    l = [0]*n
    visited[init_node] = True 
    l[0] = arr[init_node]
    dfs(init_node,cnt+1,l)

print(res)

