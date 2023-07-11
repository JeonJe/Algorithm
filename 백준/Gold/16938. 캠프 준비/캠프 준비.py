N, L, R, X = map(int,input().split())
problems = list(map(int,input().split()))
problems.sort()

def dfs(depth, idx, min_d, max_d, sum_diff):
    global answer
    if sum_diff > R:
        return 
    if depth >= 2 and L <= sum_diff <= R:
        if max_d - min_d  >= X:
            answer += 1
    
    for i in range(idx+1, N):
        if min_d == -1:
            dfs(depth+1, i, problems[i], max_d, sum_diff + problems[i])
        else:
            dfs(depth+1, i, min_d, problems[i], sum_diff + problems[i])

answer = 0
dfs(0, -1, -1, -1, 0)
print(answer)