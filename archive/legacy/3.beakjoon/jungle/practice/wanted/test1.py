import sys 
input = sys.stdin.readline

n = int(input())
stones = list(map(int, input().split()))

# 0 : 해당 인덱스의 돌상에 금칠 X
# 1 : 해당 인덱스의 돌상에 금칠 O
# col : 해당 인덱스까지 돌상 확인
# dp : 해당 인덱스까지 돌상에 금칠을 하던 안하던해서 구한 깨달음의 양

round_max = []
for j in range(len(stones)):
    dp = [ [0 for _ in range(len(stones))] for _ in range(2) ]
    dp[1][j] = 1 
    first_direction = stones[j]
    for i in range(j+1,len(stones)):
        dp[0][i] = dp[1][i-1]
        if stones[i] == first_direction:
            dp[1][i] = dp[1][i-1] + 1
        else:
            dp[1][i] = dp[1][i-1] - 1
    round_max.append(max(abs(max(dp[0])), abs(max(dp[1]))))

print(max(round_max))


