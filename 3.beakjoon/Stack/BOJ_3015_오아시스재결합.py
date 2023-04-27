n = int(input())
heights = [int(input()) for _ in range(n)]

stack = []
answer = 0

for height in heights:
    #스택에서 현재 높이보다 작은 높이들은 모두 pop
    while stack and stack[-1][0] < height:
        
        answer += stack.pop()[1]
    
    if not stack:
        stack.append([height,1])
        continue
    #스택의 top이 가지고있는 높이와 현재 확인 중인 높이가 같을경우
    if stack[-1][0] == height:
        prev_cnt = stack.pop()[1]
        answer += prev_cnt

        if stack:
            answer += 1
        stack.append([height,prev_cnt+1])
    else:
        #스택이 더 높을 경우
        stack.append((height,1))
        answer += 1
print(answer)
