
n = int(input())
if n == 1:
    print(1)
    exit()
elif n == 2:
    print(2)
    exit()

dp = [0] * (1001)
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    #i에 1x2 타일이 올경우 i에  2x1을 놓을경우
    dp[i] = (dp[i-1] + dp[i-2])% (10007)

print(dp[n])