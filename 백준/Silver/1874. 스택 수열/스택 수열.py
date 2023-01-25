n = int(input())

target = [int(input()) for _ in range(n)]
stack = []
res = []

for i in range(1,n+1):
    res.append('+')
    stack.append(i)

    while len(target) > 0 and len(stack) > 0 and stack[-1] == target[0] :        
        res.append('-')
        stack.pop()
        target.pop(0)

if len(stack) != 0:
    print("NO")
    exit()

for operation in res:
    print(operation)
