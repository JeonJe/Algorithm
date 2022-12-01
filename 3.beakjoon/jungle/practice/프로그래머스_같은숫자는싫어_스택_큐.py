def solution(arr):
    answer = []
    stack = []
    if len(arr) <= 1:
        return arr 

    stack.append(arr[0])

    for i in range(1,len(arr)):
        while len(stack) > 0 and stack[-1] == arr[i]:
            stack.pop()
        stack.append(arr[i])
    return stack


arr = [1,1,3,3,0,1,1]

print(solution(arr))