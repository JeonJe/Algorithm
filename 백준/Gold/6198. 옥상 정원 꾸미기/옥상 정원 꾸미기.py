n = int(input())
seq = [int(input()) for _ in range(n)]
stack = []
answer = 0

for i in range(n):
    while stack and seq[i] >= stack[-1]:
        stack.pop()
    stack.append(seq[i])

    answer += len(stack)-1
print(answer)