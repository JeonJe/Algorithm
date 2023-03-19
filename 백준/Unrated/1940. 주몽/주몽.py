n = int(input())
m = int(input())
items = list(map(int,input().split()))

items.sort()
left = 0
right = len(items) - 1

answer = 0
while left < right:
    s = items[left] + items[right]
    if s < m:
        left += 1
    elif s > m:
        right -= 1
    else:
        answer += 1
        left += 1
        right -= 1

print(answer)
