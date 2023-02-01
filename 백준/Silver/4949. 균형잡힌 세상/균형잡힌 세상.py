
while True:
    sentence = input()

    if sentence == ".":
        break
    stack = []
    res = "yes"
    for i in sentence:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                res = "no"
        elif i == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                res = "no"
    if len(stack) > 0:
        res = "no"
    print(res)
