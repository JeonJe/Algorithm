import sys

K = int(input())

stack = []
for _ in range(K):
    num = int(sys.stdin.readline())

    if num != 0:
        stack.append(num)
    if num == 0:
        stack.pop()

print(sum(stack))