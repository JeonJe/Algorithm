

n = int(input())
arr = list(map(int, input().split()))
arr.insert(0,0)
dp = [0] * (n+1)
seq = []
for i in range(1,n+1):
    dp_max = 0
    for j in range(1,i):
        if arr[j] <  arr[i]:
            dp_max = max(dp_max,dp[j])
    dp[i] = dp_max + 1
print(max(dp))

order = max(dp)
for i in range(n, 0,-1):
    if dp[i] == order:
        seq.append(arr[i])
        order -= 1
seq = list(reversed(seq))
print(*seq)

