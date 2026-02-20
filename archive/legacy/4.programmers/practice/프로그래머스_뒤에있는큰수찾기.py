def solution(numbers):
    answer = []
    stack = []

    #뒤에서부터 확인 
    for i in range(len(numbers)-1,-1,-1):
        #스택에 남아있는 값들 중 현재 값보다 큰 값이 있는 지 확인
        #작은 값들은 모두 pop 처리
        while stack and numbers[i] >= stack[-1]:
            stack.pop()

        #만약 스택에 아무것도 없다면 ?
        if len(stack) == 0:
            answer.append(-1)
        else:
        #현재 스택에 남아 있는 값이 더 큰 값
            answer.append(stack[-1])
        stack.append(numbers[i])

    return answer[::-1]


numbers = [9,1,5,3,6,2]

print(solution(numbers))