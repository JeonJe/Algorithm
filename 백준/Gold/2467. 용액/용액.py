import sys

n = int(input())
arr = list(map(int,input().split()))
diff = sys.maxsize
arr.sort()

left = 0
right = len(arr)-1
ans_left = 0
ans_right = 0

if len(arr) == 2:
    print(arr[0], arr[1])
    exit()

while left < right:
    mix = arr[left] + arr[right]

    if mix == 0:
        print(arr[left], arr[right])
        exit()

    if abs(mix) < diff:
        diff = abs(mix)
        ans_left = arr[left]
        ans_right = arr[right]

    if mix < 0:
        left += 1
    else:
        right -= 1

print(ans_left, ans_right)

