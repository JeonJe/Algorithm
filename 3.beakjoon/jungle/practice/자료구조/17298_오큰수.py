n = int(input())

target = list(map(int,input().split()))
stack = []
res = []
for i in range(len(target)-1,-1,-1):
    while (stack):
        if stack[-1]  > target[i]:
            res.append(stack[-1])
            break
        else:
            stack.pop()
    if not stack:
        res.append(-1)
    stack.append(target[i])

print(*res[::-1])