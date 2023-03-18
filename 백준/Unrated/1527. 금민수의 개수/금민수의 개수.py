def dfs(A,B, depth, temp):
    global answer
    if depth >= 10:
        return 
    if temp > B:
        return 
    if A <= temp <= B:
        answer += 1
    dfs(A,B,depth+1, temp*10+4)
    dfs(A,B,depth+1, temp*10+7)

A,B = map(int,input().split())

global answer
answer = 0
dfs(A,B, 0, 0)

print(answer)
