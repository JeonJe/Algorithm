
sticks = input()
stack = []

res = 0
prev = ""
for idx, s in enumerate(sticks):
    if s == "(":
        stack.append(s)
    # ')'
    else:
        stack.pop()
        prev = sticks[idx-1]
        # laser
        if prev == "(":
            res += len(stack)
        # end of stick
        else:
            res += 1
print(res)
