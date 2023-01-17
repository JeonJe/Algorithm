N,S,M = map(int,(input().split()))

dp = [[False]*(M+1) for _ in range(N+1)]
dp[0][S] = True

vol_list = list(map(int,input().split()))
vol_list.insert(0,0)

for i in range(1,len(vol_list)):
    for j in range(M+1):
        if not dp[i-1][j]:
            continue
        if j + vol_list[i] <= M:
            dp[i][j+vol_list[i]] = True
        if  j - vol_list[i] >= 0:
            dp[i][j-vol_list[i]] = True 

max_idx = -1
for j in range(M,-1,-1):
    if dp[N][j]:
        max_idx = j
        break

print(max_idx)