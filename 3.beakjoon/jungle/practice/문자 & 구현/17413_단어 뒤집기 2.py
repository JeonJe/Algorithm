
ins = input()
stack = ""
answer = ""

Tag = False
for c in ins:
    if c == "<":
        Tag = True
        answer += stack[::-1]
        answer += c
        stack = ""
        continue
    elif c == ">":
        Tag = False
        answer += c
        continue
    elif c == " ":
        answer += stack[::-1] + " "
        stack = ""
        continue
    else:
        if Tag:
            answer += c
        else:
            stack += c

print(answer+stack[::-1])

    
    
