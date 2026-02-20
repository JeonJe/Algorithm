n = int(input())
seq = [input() for _ in range(n)]
answer = 0
for i in range(len(seq)):
    stack = []
    cur = seq[i]
    for j in range(len(cur)):
        if stack and stack[-1] == cur[j]:
            stack.pop()
            continue
        stack.append(cur[j])
    if not stack:
        answer += 1
print(answer)

    
