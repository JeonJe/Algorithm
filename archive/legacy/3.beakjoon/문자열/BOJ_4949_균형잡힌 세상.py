
def check(word):
    stack = []
    for i in range(len(word)):
        if word[i] == "[" or word[i]=="(":
            stack.append(word[i])
        elif  word[i] =="]" :
            if stack and stack[-1] == "[":
              stack.pop()
            else:
                return False
        elif word[i] == ")" :
            if stack and stack[-1] == "(":
              stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True

while True:
    n = input()
    if n == ".":
        break
    
    if check(n):
        print("yes")
    else:
        print("no")
    

   
          