N = int(input())
arr = [ list(map(int,input().split())) for _ in range(N)]

dp = [0] * (N+2)

M = 0
for i in range(N):
    #t = i번째 일을 하는데 걸리는 시간
    t = arr[i][0]
    #p = i번째 일을하고 얻을 수 있는 가치
    p = arr[i][1]
    #M : 현재까지 저장된 M의 값 
    #dp[i] : i일까지 벌 수 있는 최대가치
    M = max(M, dp[i])  #이전가치와 i일까지 가치 중 큰 가치를 가져옴
    if i + t > N:
        continue
    #i일부터 t일 후에 얻을 수 있는 최대 가치는, 
    #i일까지의 최대가치 M에 i번째 일을 하고 얻을 수 있는 가치 p를 더한 값과
    #i+t일까지 얻을 수 있는 최대 가치 dp[i+t] 중 큰 값 
    dp[i+t] = max(M+p, dp[i+t])

print(max(dp))

