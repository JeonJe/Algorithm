L,C = map(int,input().split())

data = input().split()
data.sort()

def dfs(idx, path,check):
    if len(path) >= L:
        #모음의 수 
        temp = 0
        for p in path:
            if p in ["a","e","i","o","u"]:
                temp+=1
        #자음의 수 = len(path) -  모음의 수 
        if temp >= 1 and len(path) - temp >= 2:
            print("".join(path))
        return 

    for i in range(idx+1,len(data)):
        path.append(data[i])
        dfs(i,path,check)
        path.pop()
    
    return 

for i in range(len(data)):
    dfs(i,[data[i]],[False])