N, M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()

def dfs(idx, path):
    if len(path) >= M:
        print(*path)
        return 
    
    for i in range(len(nums)):
        if path[-1] <= nums[i]:
            path.append(nums[i])
            dfs(i,path)
            path.pop()

for i in range(len(nums)):
    dfs(i,[nums[i]])