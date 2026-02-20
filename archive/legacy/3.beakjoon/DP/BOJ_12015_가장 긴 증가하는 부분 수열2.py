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

length = []
length.append(nums[0])

find_seq = [[0,0] for _ in range(n)]
find_seq[0][1] = nums[0]

for i in range(1,n):
    find_seq[i][1] = nums[i]

    if nums[i] > length[-1]:
        find_seq[i][0] = len(length)
        length.append(nums[i])
        
    else:
        find_idx = lower_bound(length,nums[i])
        length[find_idx] = nums[i]
        find_seq[i][0] = find_idx

print(len(length))

answer = []
order = len(length)-1

for i in range(len(find_seq)-1,-1,-1):
    if order == -1:
        break
    elif order == find_seq[i][0]:
        answer.append(find_seq[i][1])
        order-=1
    
print(*answer[::-1])
