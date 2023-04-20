
data = input()
n = int(input())

left_stack = [i for i in data]
right_stack = []

for i in range(n):
    command_str = input()
    first_chr = command_str[0]
    if first_chr == "P":
        command, param = command_str.split()
        left_stack.append(param)
    elif first_chr == "L":
        if len(left_stack) > 0:
            right_stack.append(left_stack.pop())

    elif first_chr == "B":
        if len(left_stack) > 0:
            left_stack.pop()
    else:
        if len(right_stack) > 0:
            left_stack.append(right_stack.pop())

print("".join(left_stack) + "".join(reversed(right_stack)))
