from collections import deque 

data = input()
n = int(input())

right_que = deque()

left_stack = []
right_stack = []

for i in data:
    left_stack.append(i)

for i in range(n):
    command_str = input()
    first_chr = command_str[0]
    if first_chr == "P":
        command, param = command_str.split()
        left_stack.append(param)
    elif first_chr == "L":
        if len(left_stack) > 0:
            right_que.appendleft(left_stack.pop())

    elif first_chr == "B":
        if len(left_stack) > 0:
            left_stack.pop()
    else:
        if len(right_que) > 0:
            left_stack.append(right_que.popleft())

answer = ''
answer += "".join(left_stack) + "".join(right_que)
print(answer)
