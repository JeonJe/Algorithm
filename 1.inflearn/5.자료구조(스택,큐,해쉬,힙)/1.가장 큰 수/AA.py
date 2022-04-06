import sys

# sys.stdin = open("input.txt",'rt')

num,m = input().split()
m = int(m)
stack = [ ]

for i in range(0,len(num)):
#자기 앞에보다 작은 숫자가 있으면 지우면서 앞으로 감, 단 지울 개수가 남아있어야함.

    while stack and m>0 and stack[-1] < num[i] :
        stack.pop()
        m-=1
    stack.append(num[i])

if m>0:
    print( ''.join(stack[:-m]))
else:
    print(''.join(stack))


