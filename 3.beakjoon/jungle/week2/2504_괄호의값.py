arr = input()

stack = []

num_parentheses = 0
num_curly = 0

for i in range(len(arr)):
    if arr[i] == "(":
        stack.append("(")
        num_parentheses += 1
    elif arr[i] == ")":
        num_parentheses = 0
    elif arr[i] == "[":
        num_curly += 1
    elif arr[i] == "]":
        num_curly = 0