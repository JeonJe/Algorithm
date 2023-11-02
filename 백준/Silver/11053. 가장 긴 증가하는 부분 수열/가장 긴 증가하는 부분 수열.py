
n = int(input())
seq = list(map(int,input().split()))

#i번째에서 가장 긴 증가하는 부분수열의 길이
dp = [0] *(n+1)
dp[0] = 1

for i in range(1,n):
    longest = 0
    for j in range(i-1,-1,-1):
        if seq[j] < seq[i]:
            longest = max(longest, dp[j])
    dp[i] = longest + 1

print(max(dp))
