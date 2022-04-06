

import sys

# N = int(input())

# MAX = 9999999
# dp = [ 9999999 for i in range(5000+1) ]

# dp[3] = 1
# dp[5] = 1

# for i in range(6,N+1):
#     dp[i] = min(dp[i-3],dp[i-5])+1

# print(dp[N] if dp[N] < MAX else -1 )
    

############################################
cnt  = 0

while True:
    if N % 5 == 0:
        Q = N // 5
        R = N % 5
        N = R 
        cnt+=Q 
        print(cnt)
        break
    else:
        N -= 3
        cnt+=1
        if N < 0:
            print(-1)
            break




