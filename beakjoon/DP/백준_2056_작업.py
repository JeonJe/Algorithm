n = int(input())
dp= [0]*(n+1)

#n개 만큼 반복문 1부터 n까지
for i in range(1,n+1):
    temp = list(map(int,input().split()))
    cur_t = temp[0]

    max_time = 0
    for j in range(temp[1]):
        max_time = max(max_time,dp[temp[j+2]])
        #선행 작업이 완료된 시간 의 최대값

    dp[i] = max_time + cur_t

print(max(dp))



