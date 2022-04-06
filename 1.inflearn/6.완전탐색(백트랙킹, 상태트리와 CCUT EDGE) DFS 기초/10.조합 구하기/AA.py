import sys

# sys.stdin = open('input.txt','r')
def dfs(L,S):
    global cnt
    if L==M:
        for i in range(L):
            print(res[i],end=' ')
        print()
        cnt+=1
    else:
        for j in range(S,N+1):
            res[L] = j
            dfs(L+1,j+1)

N,M = map(int,input().split())

res = [0]*(N+1)
cnt = 0
dfs(0,1)
print(cnt)