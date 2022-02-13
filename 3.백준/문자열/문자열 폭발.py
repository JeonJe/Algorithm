string = input()
bomb = input()

lastBombChar = bomb[-1]
stack = []
strlen = len(bomb)

for c in string:
    stack.append(c)
    if c == lastBombChar and ''.join(stack[-strlen:]) == bomb:
        del stack[-strlen:]

answer = ''.join(stack)

if answer == '':
    print("FRULA")
else:
    print(answer)

