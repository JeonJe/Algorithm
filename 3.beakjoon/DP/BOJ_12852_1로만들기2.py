
n = int(input())

dp = [1e9] *(n+5)
prev_idx = [1e9] *(n+5)
prev_idx[1] = 1
#i부터 1을 만들기 위한 연산 횟수 
dp[0],dp[1] = 0,0

temp = []

for i in range(2,n+5):
    if i % 3 == 0:
        if dp[i//3]+1 < dp[i]: 
            dp[i] = dp[i//3]+1
            prev_idx[i] = i // 3

    if i % 2 ==0:
        if dp[i//2]+1 < dp[i]: 
            dp[i] = dp[i//2]+1
            prev_idx[i] = i // 2

    if dp[i-1]+1 < dp[i]: 
        dp[i] = dp[i-1]+1
        prev_idx[i] = i -1

    

print(dp[n])
print(n,end=' ')

while n != 1:
    n = prev_idx[n]
    print(n,end=' ')


