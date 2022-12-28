
#수열의 길이 M
N,M = map(int,input().split())

nums = [i for i in range(1,N+1)]


def dfs(start, depth, temp):
    if depth == M:
        print(*temp)
        return 
    
    for i in range(start,len(nums)+1):
        temp.append(i)
        dfs(i,depth+1, temp)
        temp.remove(i)

for i in nums:
    dfs(i,1, [i])