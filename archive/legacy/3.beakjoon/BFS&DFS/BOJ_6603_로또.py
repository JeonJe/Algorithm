def dfs(idx, path):
    if len(path) >= 6:
        print(*path)
        return
    
    for i in range(idx+1,len(nums)):
        path.append(nums[i])
        dfs(i,path)
        path.pop()

while True:
    data = input()
    if data[0] == "0":
        break
    data = list(map(int,data.split()))
    k, nums = data[0], data[1:]
    nums.sort()

    for i in range(len(nums)):
        dfs(i, [nums[i]])
    print()