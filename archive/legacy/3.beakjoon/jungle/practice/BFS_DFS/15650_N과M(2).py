N, M = map(int,input().split())

nums = [i for i in range(1,N+1)]

def dfs(start_idx, path):
    if len(path) >= M:
        print(*path)
        return 
    
    for i in range(start_idx+1, len(nums)):
        path.append(nums[i])
        dfs(i, path)
        path.pop()

for i in range(len(nums)):
    dfs(i,[nums[i]])