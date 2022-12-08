def solution(number, k):

    number = list(number)
    stack = []
    stack.append(number[0])
    res = []
    cnt = 0
    for i in range(1,len(number)):
        
        while cnt < k and stack and stack[-1] < number[i]:
            stack.pop()
            cnt += 1
        stack.append(number[i])
    if len(stack) == len(number):
        stack = stack[:len(number)-k]
    return ''.join(stack)
    

