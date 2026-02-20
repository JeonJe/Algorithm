n = input()

stack = []

cnt = 0
for i in range(len(n)):
    if n[i] == "(" or n[i] =="[":
        stack.append(n[i])
    elif n[i] ==")" :
      if stack and stack[-1] =="(":
        stack.pop()
      else:
         stack.append(n[i])
    elif n[i] == "]":
      if stack and stack[-1] == "[":
          stack.pop()
      else:
        stack.append(n[i])
print(len(stack))
