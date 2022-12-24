from collections import deque
n = int(input())
arr = list(map(int,input().split()))
arr.insert(0,0)
dp = [0] * (1001)
dp[1] = 1

stack = deque()

for i in range(2,n+1):
    max_temp = 0
    que.append(arr[i])
    #현재 확인중인 인덱스보다 작은 인덱스들을 확인하여
    #조건을 만족하는 가장 긴 부분수열의 값을 찾음
    for k in range(i-1, 0, -1):
        if arr[i] > arr[k]:
            max_temp = max(max_temp,dp[k])
            
    dp[i] = max_temp + 1

# print(dp)
print(max(dp))