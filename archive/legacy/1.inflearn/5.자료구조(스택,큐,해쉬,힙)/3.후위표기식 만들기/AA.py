import sys

# sys.stdin = open("input.txt",'rt')  

str = input()
stack = []

for s in str:



# 1. 숫자가 나오면 그대로 출력한다.
    if s.isnumeric():
        print(s,end='')

# 2. (나오면 스택에 push한다.
# 3. * / 나오면 스택에 push한다.
    elif s == '(' or s == '*' or s=='/':
        stack.append(s)

# 4. + - 연산이 나오면 여는 괄호('('), 여는 괄호가 없다면 스택의 끝까지 출력하고 그 연산자를 스택에 push한다.

    elif s == '+' or s=='-' or s == ')':
        while len(stack) > 0 and stack[-1] != '(' :
            print(stack[-1],end='')
            stack.pop()
        if s == '+' or s=='-':
            stack.append(s)
# 5. 닫는 괄호(')')가 나오면 여는 괄호('(')가 나올때까지 pop하여 출력한다.
        else:
            #여는 괄호('(') pop
            stack.pop()

if len(stack) > 0 :
    print(*stack)
