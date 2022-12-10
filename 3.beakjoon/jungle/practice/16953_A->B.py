A,B = map(int,input().split())



def dfs(x,cnt):
    
    if x == B:
        print(cnt)
        exit()
    if x > B:
        return 
    dfs(x*2,cnt+1)
    next_num = int(str(x)+'1')
    dfs(next_num,cnt+1)

dfs(A,1)
print(-1)

# dfs(B//2)
# dfs(B//10)