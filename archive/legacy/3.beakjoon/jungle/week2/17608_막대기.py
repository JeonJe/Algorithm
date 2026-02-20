import sys
N = int(input())

stack = [int(sys.stdin.readline()) for _ in range(N)]

prev = stack[-1]
cnt = 1
while len(stack) > 0:
    cur = stack.pop()

    if cur > prev:
        cnt+=1
        prev = cur 

print(cnt)