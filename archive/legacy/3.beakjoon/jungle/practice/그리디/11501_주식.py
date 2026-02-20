
T = int(input())
for _ in range(T):
    N = int(input())
    prices = list(map(int,input().split()))
    
    top = prices[-1]
    cnt = 0
    for i in range(len(prices)-2,-1,-1):
        if prices[i] >= top:
            top = prices[i]
        else:
            cnt += top - prices[i]
    print(cnt)


