n = int(input())

sequen = [int(input()) for _ in range(n)]
origin = [i+1 for i in range(n)]

stack = []
answer = []
j = 0

for i in range(len(origin)):
    stack.append(origin[i])
    answer.append("+")

    while stack and stack[-1] == sequen[j]:
        stack.pop()
        answer.append("-")
        j+=1

if stack:
    print("NO")
    exit()
for seq in answer:
    print(seq)


