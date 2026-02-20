n, k = map(int,input().split())
coins = [ int(input()) for _ in range(n) ]

cnt = 0
while k != 0:
    for i in range(n-1,-1,-1):
        if coins[i] <= k:
            k -= coins[i]
            cnt+=1
            break
M = 0
for i in range(n-1, -1, -1):
    M += k // coins[i] 
    k = k % coins[i]
print(M)