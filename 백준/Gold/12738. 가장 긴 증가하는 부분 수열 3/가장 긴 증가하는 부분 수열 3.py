import sys
input = sys.stdin.readline 

n = int(input())
nums = list(map(int,input().split()))

def lower_bound(arr, key):
    left, right = 0,len(arr)-1
    
    while (left < right):
        mid = left + (right - left) // 2

        if arr[mid] < key:
            left = mid+1
        else:
            right = mid 

    return right 

answer = []
answer.append(nums[0])

for i in range(1,n):
    if nums[i] > answer[-1]:
        answer.append(nums[i])
    else:
        idx = lower_bound(answer,nums[i])
        answer[idx] = nums[i]

print(len(answer))