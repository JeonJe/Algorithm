n = int(input())

stairs = [ int(input()) for _ in range(n)]
stairs.insert(0,0)
dp = [0]*301
if n == 1:
    print(stairs[1])
    exit()

dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]

for i in range(3,n+1):
    #경우1 
    #마지막 n번째 칸을 1칸 전에서 올라 올 경우 -> n-1칸은 n-3칸에서 올라와야함
    #경우2 마지막 n번째 칸을 2칸 전에서 올라 올 경우 
    dp[i] = max(dp[i-3]+stairs[i-1],dp[i-2]) + stairs[i]

print(dp[n])