import sys
input = sys.stdin.readline 

answers = list(map(int,input().split()))

def dfs(depth, path, correct):
    global answer
    if depth >= 10:
        if correct >= 5:
            answer += 1
        return 
    
    for i in range(1,6):
        #3개의 연속된 답은 스킵 
        if len(path) >= 2 and path[-1] == path[-2] and path[-1] == i:
            continue

        path.append(i)
    
        #현재 답을 맞춘경우 맞춘 갯수 증가 
        if i == answers[depth]:
            dfs(depth+1, path, correct+1)    
        else:
            dfs(depth+1, path, correct)    
        
        path.pop()
            
answer = 0
dfs(0,[],0)
print(answer)