N = int(input())

sequence = list(map(int,input().split()))
dp = [0] * (N+1)
dp[0] = 1

for i in range(1,N):
    m = 0
    for j in range(i-1,-1,-1):
        if sequence[j] < sequence[i]:
            m = max(m, dp[j])
    dp[i] = m+1

print(max(dp))