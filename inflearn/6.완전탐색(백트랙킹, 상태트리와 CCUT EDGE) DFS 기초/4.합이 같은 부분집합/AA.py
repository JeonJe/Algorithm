import sys
# sys.stdin = open("input.txt",'rt') 

def dfs(Depth,Sum):
    if Sum > TotalSum // 2:
        return 
    if Depth == N:
        if Sum == (TotalSum - Sum):
            print("YES")
            sys.exit(0)
    else:
        dfs(Depth+1, Sum+arr[Depth])
        dfs(Depth+1, Sum)

N = int(input())
arr = list(map(int,input().split()))
TotalSum = sum(arr)
dfs(0,0)    
print("NO")