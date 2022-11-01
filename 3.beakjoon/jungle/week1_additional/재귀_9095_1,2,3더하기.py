t = int(input())

global cnt 

cnt = 0
arr = [1,2,3]

def dfs(depth, sum):
    global cnt 
    if sum > n:
        return 
    elif sum == n:
        cnt += 1

    else:
        for i in range(3):    
            dfs(depth+1, sum+arr[i] )



for i in range(t):
    n = int(input())
    cnt = 0
    dfs(0,0)
    print(cnt)