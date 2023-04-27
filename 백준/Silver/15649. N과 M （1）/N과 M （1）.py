N, M = map(int,input().split())
seq = [ i for i in range(N+1) ]

def dfs(depth,start,temp):
    
    if len(temp) == M:
        print(*temp)
        return 

    for i in range(1, N+1):
        if i in temp:
            continue

        temp.append(seq[i])
        dfs(depth+1,start,temp)
        temp.remove(seq[i])

for i in range(1,N+1):
        dfs(0,i, [i])