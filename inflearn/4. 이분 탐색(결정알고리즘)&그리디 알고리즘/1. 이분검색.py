import sys

def binary_search(nums,target):
    res = []
    left,right = 0, len(nums)-1
    
    while left <= right:
        mid = (left+right )// 2
        if nums[mid] == target:
            return mid

        elif nums[mid] > target:
            right = mid-1
        else:
            left = mid+1
        
    return -1

    
# sys.stdin=open("input.txt","r")
N,M = map(int,input().split())

nums = list(map(int,input().split()))
nums.sort()
print(binary_search(nums,M)+1)
