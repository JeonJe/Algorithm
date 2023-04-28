from collections import defaultdict 

N,M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()

visited = [False]*(N)
checked = defaultdict(int)

def dfs(idx,path):
    if len(path) >= M:
        if checked[".".join(list(map(str,path)))] == 0:
            print(*path)
            checked[".".join(list(map(str,path)))]+= 1
        return 
    
    for i in range(len(nums)):
        if not visited[i]:
            visited[i] = True
            path.append(nums[i])
            dfs(i,path)
            path.pop()
            visited[i] = False


for i in range(len(nums)):
    visited[i] = True
    dfs(i,[nums[i]])
    visited[i] = False
