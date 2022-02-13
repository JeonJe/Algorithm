
x = int(input())

dp = [0] * 300001

for i in range(2,x+1):
    #현재의 수에서 1을 빼는 경우
    dp[i] = dp[i-1]+1
    #현재의 수가 2로 나누어 떨어지는 경우

    #dp[i] 는 1을 뺴는 경우이므로 +1 연산 횟수 추가
    #dp[i//2]+1 는 i//2 에서 곱하기 2이므로  +1 연 횟수 추가
    if i % 2 == 0 :
        dp[i] = min(dp[i], dp[i//2]+1)
    # 현재의 수가 3로 나누어 떨어지는 경우
    elif i % 3 == 0 :
        dp[i] = min(dp[i], dp[i//3]+1)
    # 현재의 수가 5로 나누어 떨어지는 경우
    elif i % 5 == 0 :
        dp[i] = min(dp[i], dp[i//5]+1)

print(dp[x])