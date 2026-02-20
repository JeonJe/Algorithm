stack1 = list(input())
stack2 = []
n = int(input())
commands = [ input() for _ in range(n) ]

for command in commands:
    c = ""
    if len(command) > 1:
        command, c = command.split()
    if command == 'L':
        if stack1:
            stack2.append(stack1.pop())
    elif command == 'D':
        if stack2:
            stack1.append(stack2.pop())
    elif command == 'B':
        if stack1:
            stack1.pop()
    else:
        stack1.append(c)

stack1.extend(reversed(stack2))
print( ''.join(stack1))
   

            
    
