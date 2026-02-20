<<<<<<< HEAD
#계산을 저장하기 위한 dp 테이블 초기화

dp = [0] *100

dp[1] = 1
dp[2] = 2

for i in range(3,n+1):
=======
#계산을 저장하기 위한 dp 테이블 초기화

dp = [0] *100

dp[1] = 1
dp[2] = 2

for i in range(3,n+1):
>>>>>>> 65f2ee7131e2912c03d2122a15fcc235b3105750
    dp[i] = dp[[i-1] + dp[i-2]]