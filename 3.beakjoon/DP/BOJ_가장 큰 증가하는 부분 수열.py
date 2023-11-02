
n = int(input())
seq = list(map(int, input().split()))

dp = [0] * (n+1)

#i번째까지 증가하는 부분 수열의 최대 값
dp[0] = seq[0]

for i in range(1,len(seq)):
    max_sum = 0
    for j in range(0,i):
        if seq[j] < seq[i]:
            max_sum = max(max_sum, dp[j])
    dp[i] = max_sum+seq[i]

print(max(dp))
