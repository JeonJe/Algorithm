

def solution(s):
    def isRight(target):
        stack = []
        leftside = ["[", "{", "("]

        for i in target:
            if i in leftside:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                elif i == "]" and stack[-1] == "[":
                    stack.pop()
                elif i == "}" and stack[-1] == "{":
                    stack.pop()
                elif i == ")" and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
        if len(stack) > 0 :
            return False
        return True

    answer = 0
    temp_s = list(s)
    for i in range(len(temp_s)):
        shift_s = temp_s[i:] + temp_s[:i]
        if isRight(shift_s):
            answer +=1

    return answer


s = "}]()[{"
print(solution(s))