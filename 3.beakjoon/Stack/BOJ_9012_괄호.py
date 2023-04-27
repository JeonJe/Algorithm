import sys
input = sys.stdin.readline

t = int(input())
VPS = {
    ')' : '('
}
for _ in range(t):
    target = input().rstrip()
    stack = []
    answer = "YES"
    for j in range(len(target)):
        if target[j] == '(':
            stack.append('(')
        else:
            if stack and stack[-1] == VPS[target[j]]:
                stack.pop()
            else:
                answer = "NO"
    if stack:
        answer = "NO"
    print(answer)
    
