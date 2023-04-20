import sys 
input = sys.stdin.readline
n = int(input())
numbers = list(map(int,input().split()))
numbers.insert(0,0)
dp = [[0 for _ in range(21) ] for _ in range(n) ]

#dp[i][j] => i번째 수까지 사용하여 j의 값을 만들 수 있는 조합의 수 (k)
dp[1][numbers[1]] += 1

for i in range(2,n):
    for j in range(21):
        #j값을 만들 수 없으면 그 조합을 계산할 때 사용할 수 없기 때문에 continue
        if dp[i-1][j] == 0:
            continue
        
        if j + numbers[i]  <= 20:
            
            #0부터 i까지 j+numbers[i]를 만들 수 있는 가짓수는 0부터 i-1까지 j를 만들 수 있는 경우를 포함한다.
            #0~i-1까지 조합으로 j를 만들고, 지금 확인하고 있는 i를 사용하여 j+numbers[i]의 수를 만들 수 있다는 뜻
            dp[i][j+numbers[i]] += dp[i-1][j]
            
        if j - numbers[i] >= 0:
            dp[i][j-numbers[i]] += dp[i-1][j]

print(dp[n-1][numbers[-1]])




