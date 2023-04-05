def solution(ingredient):
    answer = 0
    stack = []

    for i in range(len(ingredient)):
        if ingredient[i] != 1 :
            stack.append(ingredient[i])
        else:
            #스택의 마지막 4개가 빵야채고기빵 순서이면
            if len(stack) >= 3 and ''.join(map(str,stack[-3:])) == "123":
                answer += 1
                for _ in range(3):
                    stack.pop()
            else:
                stack.append(ingredient[i])
    return answer
        


ingredient = [1, 3, 2, 1, 2, 1, 3, 1, 2]
print(solution(ingredient))