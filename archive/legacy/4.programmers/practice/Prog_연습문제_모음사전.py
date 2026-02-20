target = ["A","E","I","O","U"]

def dfs(depth, path, word):
    global answer 
    answer += 1 
    idx = 0
    
    if "".join(path) == word:
        return answer 
    
    if len(path) >= len(target):
        return 0    
    
    for i in range(len(target)):
        path.append(target[i])
        idx += dfs(depth+1, path, word)
        if idx > 0:
            return idx
        path.pop()
    
    return idx
        
def solution(word):
    global answer 
    answer = 0
    idx = 0
    cnt = 0
    
    for i in range(len(target)):
        path = [target[i]]
        idx = dfs(0, path,  word)
        if idx > 0:
            return idx
        path.pop()
