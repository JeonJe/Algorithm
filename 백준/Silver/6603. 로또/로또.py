
def dfs (depth,temp,S):        
    if len(temp) == 6:
        print(*temp)
        return 

    if depth >= len(S):
        return 
    
    temp.append(S[depth])
    dfs(depth+1,temp,S) 
    temp.pop()

    #dpeht의 숫자를 선택하지 않거나 
    dfs(depth+1,temp,S)

while True :
    commands = list(map(int,input().split()))
    if commands[0]  == 0:
        break 
    
    k = commands[0]
    S = commands[1:]
    temp = [] 
    dfs(0,temp,S)
    print()
