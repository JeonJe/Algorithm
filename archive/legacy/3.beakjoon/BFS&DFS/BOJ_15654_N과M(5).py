N, M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
def dfs(path):
    if len(path) >= M:
        print(*path)
        return 
    for i in range(len(nums)):
        if nums[i] not in path:
            path.append(nums[i])
            dfs(path)
            path.pop()

    

for i in range(len(nums)):
    dfs([nums[i]])

