import copy 
n = int(input())
nums = map(int,input().split())

copy_nums = copy.deepcopy(nums)
copy_nums = list(set(copy_nums))
copy_nums.sort()

def binary_search(arr,v):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left+right) // 2

        if arr[mid] == v:
            return mid
        elif arr[mid] > v:
            right = mid-1
        else:
            left = mid+1
            
for i in nums:
    print(binary_search(copy_nums,i),end=' ')