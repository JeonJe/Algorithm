
def dfs(depth, temp, visited,number):
    global res
 
    if len(temp) == 3:
        if sum(temp) == 0:
            res += 1
        return
        
    if depth >= len(number):
        return

    #선택 
    temp.append(number[depth])
    visited[depth] = True
    dfs(depth+1, temp, visited,number)

    #미선택 
    temp.pop()
    visited[depth] = False
    dfs(depth+1, temp, visited,number)

def solution(number):
    global res
    res = 0
    temp = []
    visited = [False] * (len(number))
    dfs(0,temp,visited,number)

    return res