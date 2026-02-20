n = int(input())
arr = list(map(int,input().split()))
arr.sort()
x = int(input())

left, right = 0, len(arr) - 1
answer = 0

while left < right:
    if arr[left] + arr[right] == x:
        answer += 1
        left+=1
    elif arr[left] + arr[right] > x:
        right -= 1
    else:
        left +=1
print(answer)
