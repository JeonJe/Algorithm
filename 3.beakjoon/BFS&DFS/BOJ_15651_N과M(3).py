
N,M = map(int,input().split())
nums = [i for i in range(1,N+1)]

def dfs( path):
    if len(path) >= M:
        print(*path)
        return 
    
    for i in range(len(nums)):
        path.append(nums[i])
        dfs(path)
        path.pop()

for i in range(len(nums)):
    dfs([nums[i]])