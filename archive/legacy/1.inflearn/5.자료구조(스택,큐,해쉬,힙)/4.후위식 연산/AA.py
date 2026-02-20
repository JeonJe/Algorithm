import sys

# sys.stdin = open("input.txt",'rt')  

str = input()
stack = []

for s in str:

# 1. 숫자가 나오면 그대로 출력한다.
    if s.isnumeric():
        stack.append(s)
    else:
        if len(stack)>=2:
            first = int(stack.pop())
            second = int(stack.pop())
        if s=='*':
            n = second * first
        elif s=='/':
            n = second / first
        elif s=='+':
            n = second + first
        elif s=='-':
            n = second - first
        stack.append(n)

print(*stack)

