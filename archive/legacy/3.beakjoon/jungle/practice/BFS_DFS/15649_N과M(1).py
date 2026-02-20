N, M = map(int,input().split())
nums = [i for i in range(1,N+1)]

def dfs(path):
    
    if len(path) >= M:
        print(*path)
        return 

    for j in range(len(nums)):
        if nums[j] not in path:
            path.append(nums[j])
            dfs(path)
            path.pop()
    

for i in range(0,len(nums)):
    dfs([nums[i]])




