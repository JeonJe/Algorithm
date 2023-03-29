n = int(input())

arr = [ float(input()) for _ in range(n)] 
dp = [0] * (n)
dp[0] = arr[0]

for i in range(1,n):
    #연속 곱에 현재 수를 곱하거나, 이번 수만 선택
    dp[i] = max(arr[i], dp[i-1]* arr[i])

print(f'{round(max(dp),3):.3f}')