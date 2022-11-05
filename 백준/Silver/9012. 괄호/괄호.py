import sys 

T = int(input())


def VPS(target):
    for i in range(len(target)):
        if data[i] == "(":
            stack.append('(')
        elif data[i] == ")":
            if len(stack) >= 1 and stack[-1] == "(":
                stack.pop()
            else:
                return False
    if len(stack) > 0: return False
    else: return True 

for _ in range(T):
    data = sys.stdin.readline()
    stack=[]
    print("YES" if VPS(data) else "NO")
    