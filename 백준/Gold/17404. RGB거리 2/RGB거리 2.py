import sys 

n = int(input())

street = [ list(map(int,input().split())) for _ in range(n) ]

dp_min = sys.maxsize
#색깔을 저장해놔야 함 
res = sys.maxsize
for k in range(3):
    dp = [ [sys.maxsize] * 3 for _ in range(n) ]
    dp[0][k] = street[0][k]
    for j in range(1,n):
        if j == n-1:
            # 첫번째 집의 색이 k이면 이면 n에서는 k번째 색을 택할 수 없음
            if k == 0:
                dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + street[j][1]
                dp[j][2] = min(dp[j-1][0], dp[j-1][1]) + street[j][2]
            elif k == 1:
                dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + street[j][0]
                dp[j][2] = min(dp[j-1][0], dp[j-1][1]) + street[j][2]
            else:
                dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + street[j][0]
                dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + street[j][1]
        else:
                dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + street[j][0]
                dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + street[j][1]
                dp[j][2] = min(dp[j-1][0], dp[j-1][1]) + street[j][2]
    dp_min = min(min(dp[n-1]),dp_min)

print(dp_min)