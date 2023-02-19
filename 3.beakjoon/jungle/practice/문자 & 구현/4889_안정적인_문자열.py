
t = 1
while True:
    
    data = input()

    if "-" in data:
        break
    stack = []
    res = 0
    for d in data:
        if d == "{":
            stack.append("{")
        else:
            if not stack:
                res += 1
                stack.append("{")
            else:
                stack.pop()

    if stack:
        res += stack.count("{") // 2
    
    print(f'{t}. {res}')        
    t += 1