n = int(input().rstrip())
seq = list(map(int,input().split()))
stack = []

answer = []
for i in range(len(seq)-1,-1,-1):
    while stack and stack[-1] <= seq[i]:
        stack.pop()
        
    if not stack:
        answer.append(-1)
    else:
        answer.append(stack[-1])
    stack.append(seq[i])

print(*reversed(answer))
    