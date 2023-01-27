import sys
input = sys.stdin.readline
n = int(input())

que = []
for _ in range(n):
    command_line = input().strip('\n')
    if " " in command_line:
        command, arg = command_line.split(" ")
    else:
        command = command_line
    if command == "push":
        que.append(arg)
    elif command == "pop":
        if que:
            print(que.pop(0))
        else:
            print(-1)
    elif command == "size":
        print(len(que))
    elif command == "empty":
        if que:
            print(0)
        else:
            print(1)
    elif command == "front":
        if que:
            print(que[0])
        else:
            print(-1)
    elif command == "back":
        if que:
            print(que[-1])
        else:
            print(-1)