
info = list(input())
bomb = list(input())

stack = []

for ch in info:
    stack.append(ch)

    if stack[-1] == bomb[-1] and ''.join(bomb) == ''.join(stack[-len(bomb):]):
        del stack[-len(bomb):]

print(''.join(stack) if len(stack) > 0 else "FRULA")
