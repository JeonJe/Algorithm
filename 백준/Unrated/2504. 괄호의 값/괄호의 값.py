S = list(input())
stack = []
answer = 0
temp = 1

for idx, char in enumerate(S):
    if char == "(":
        stack.append(char)
        temp *= 2
    elif char == "[":
        stack.append(char)
        temp *= 3
    elif char == ")":
        if not stack or stack[-1] == "[":
            print(0)
            exit()
        if S[idx-1] == "(":
            answer += temp 
        stack.pop()
        temp //= 2
        
    else:
        #case : char == "]" 
        if not stack or stack[-1] == "(":
            print(0)
            exit()
        if S[idx-1] == "[":
            answer += temp  
        stack.pop()
        temp //= 3

print(answer if not stack else 0)