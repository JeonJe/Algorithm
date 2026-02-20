from collections import defaultdict 

N,M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()

checked = defaultdict(int)

def dfs(idx,path):
    if len(path) >= M:
        if checked[".".join(list(map(str,path)))] == 0:
            print(*path)
            checked[".".join(list(map(str,path)))]+= 1
        return 
    
    for i in range(idx+1,len(nums)):
        path.append(nums[i])
        dfs(i,path)
        path.pop()


for i in range(len(nums)):
    dfs(i,[nums[i]])
