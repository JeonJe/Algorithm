from collections import defaultdict


N,P,Q = map(int,input().split())
global dict
dict = defaultdict(int)
dict[0] = 1
dict[1] = 2

def dfs(N):
    global dict 
    if dict[N]:
        return dict[N]
    else:
        dict[N] = dfs(N//P) + dfs(N//Q)
        return dict[N]

dfs(N)

print(dict[N])