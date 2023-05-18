def is_valid(x):
    for i in range(x):
        #이전 행과 현재 x행 놓은 퀸이 같은 열 또는 대각선에 있으면 안됌
        if (rows[x] == rows[i]) or abs(x-i) == abs(rows[x]- rows[i]):
            return False
    return True 

def dfs(depth):
    if depth == n:
        global answer
        answer += 1
        return 
    
    for i in range(n):
        rows[depth] = i
        if is_valid(depth):
            dfs(depth+1)


t = int(input())

for test_case in range(1,t+1):
    global answer 
    answer = 0
    n = int(input())
    rows = [-1] * (n)
    
    dfs(0)
    print(f'#{test_case} {answer}')