
N,M = map(int,input().split())
nums = [i for i in range(1,N+1)]

def dfs(idx, path):
    if len(path) >= M:
        print(*path)
        return 

    for i in range(len(nums)):
        if idx <= nums[i]:
            path.append(nums[i])
            dfs(nums[i],path)
            path.pop()

for i in range(len(nums)):
    dfs(nums[i], [nums[i]])

