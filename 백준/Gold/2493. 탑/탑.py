import sys 

n = int(input())
arr = list(map(int,sys.stdin.readline().split()))

stack = []
res = [0] * n 

stack.append( (arr[0], 1 ))

for i in range(1,len(arr)):
    if arr[i] > stack[-1][0]:
        while (len(stack)>0) and arr[i] > stack[-1][0]:
            stack.pop()
        if len(stack) == 0:
            res[i] = 0
        else:
            res[i] = stack[-1][1]
            if stack[-1][0] == arr[i]:
                stack.pop()
    else:
        res[i] = stack[-1][1]
    stack.append((arr[i],i+1))

print(*res)
