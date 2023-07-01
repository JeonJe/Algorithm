def is_balanced(target):
    left_cnt = target.count("(")
    right_cnt = target.count(")")

    if left_cnt == right_cnt:
        return True 
    else:
        return False
    
def is_right(target):
    stack = []

    for i in range(len(target)):
        if target[i] == "(":
            stack.append(target[i])
        else:
            if stack and stack[-1] == "(":
                stack.pop()
    
    if stack:
        return False
    else:
        return True 

def solution(p):
    if p == "" or is_right(p):
        return p 
    
    u, v, result = "", "", ""
    for i in range(2,len(p)+1):
        u = p[0:i]
        v = p[i:]
        
        if is_balanced(u): 
            break

    if is_right(u):
        result += u + solution(v)
    else:

        result += "("+ solution(v) + ")"
        for i in range(1,len(u)-1):
            if u[i] == "(":
                result += ")"
            else:
                result += "("
    return result 
    
    

input_list =  [")(" ,"()))((()"	]
for p in input_list:
    print(solution(p))