#계산을 저장하기 위한 dp 테이블 초기화

dp = [0] *100

dp[1] = 1
dp[2] = 2

for i in range(3,n+1):
    dp[i] = dp[[i-1] + dp[i-2]]