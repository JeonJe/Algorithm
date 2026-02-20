N = int(input())
mine = list(map(int,input().split()))
mine.sort()

M = int(input())
target = list(enumerate( list(map(int,input().split()))))
target.sort(key= lambda x : x[1])
res = [0]*(M)

def binarySerach(nums, target):
    left = -1
    right = len(nums)
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return True
        elif nums[mid] < target:
            left = mid 
        else:
            right = mid 
    return False

for idx, t in target:
    if binarySerach(mine, t):
        res[idx] = 1
    else:
        res[idx] = 0
print(*res)



