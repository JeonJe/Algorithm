
for i in range(int(input())):
    data = input()
    left_stack = []
    right_stack = []

    for chr in data:
        if chr == "<":
            if left_stack:
                right_stack.append(left_stack.pop())
        elif chr == ">":
            if right_stack:
                left_stack.append(right_stack.pop())
        elif chr == "-":
            if left_stack:
                left_stack.pop()
        else:
            left_stack.append(chr)
    print("".join(left_stack)+"".join(reversed(right_stack)))