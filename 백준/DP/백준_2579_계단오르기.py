

import sys

# sys.stdin = open("input.txt",'rt')
N = int(input())
arr = []
arr.append(0)
for i in range (N):
    arr.append(int(input()))

if N == 1:
    print(arr[1])
else:
    dp = [0]*301
    #첫 계단은 1칸으로만 오를 수 있음
    dp[1] = arr[1]
    #두 번째 계단의 최대 값은 한번에 두칸을 오르는 경우가 아닌 첫 계단과 두번째 계단 모두 밟는 경우
    dp[2] = arr[1] + arr[2]

    for i in range(3,N+1):
        #경우1 마지막 n번째 칸을 1칸 전에서 올라 올 경우 -> n-1칸은 n-3칸에서 올라와야함
        #경우2 마지막 n번째 칸을 2칸 전에서 올라 올 경우 
        dp[i] = max(dp[i-3]+arr[i-1],dp[i-2])+arr[i]
        
    
    print(dp[N])