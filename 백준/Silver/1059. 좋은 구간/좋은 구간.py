n = int(input())

nums = list(map(int,input().split()))
nums.insert(0,0)
nums.insert(len(nums),1001)
target = int(input())
global res 
res = []
def in_range(n, start, end = 0):
    return start <= n <= end if end >= start else end <= n <= start

def check(left,right,target):
    cnt = 0
    global res
    include = False
    for i in range(left+1,right-1):
        for j in range(i+1,right):
            if i<=target<=j:
                for num in nums:
                    if in_range(num, i, j):
                        include = True
                        break
                if not include:
                    res.append((i,j))

                else:
                    include = False


for i in range(len(nums)-1):
    left = nums[i]
    right = nums[i+1]

    if left < target < right:
        check(left,right,target)

temp = len(list(set(res)))
# temp = len(res)
print( temp if temp > 0 else 0 )