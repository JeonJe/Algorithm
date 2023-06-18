def BNP(init_cache, prices):
    remain = init_cache
    buy_cnt = 0
    #14일치 주식에 대해서 
    #현재 가지고 있는 현금으로 주식을 살 수 있으면 가능한 만큼 주식 구매
    #현금 감소
    for current in prices:
        if current <= remain:
            buy_cnt += remain // current
            remain %= current
    
    return remain + buy_cnt * prices[-1]

def TIMING(init_cache, prices):
    remain = init_cache
    increase = 0
    decrease = 0

    #가지고 있는 돈으로 현재 주식을 전부 사거나, 가지고 있는 주식을 전부 팔거나     
    prev = prices[0]
    buy_cnt = 0
    for i in range(1, len(prices)):
        #주가 하락
        if prev > prices[i]:
            decrease += 1
            increase = 0
        #주가 상승
        elif prev < prices[i]:
            increase += 1
            decrease = 0
        #주가 동일 -> 초기화
        else:
            increase, decrease = 0, 0
        #3일째 하락한다면 전량 매수 
        if decrease >= 3:
            if remain >= prices[i]:
                buy_cnt += remain // prices[i]
                remain %= prices[i]
            

        elif increase >= 3:
            #현재 소유한 주식이 3일째 상승한다면 전량 매도 
            if buy_cnt > 0:
                remain += buy_cnt * prices[i]
                buy_cnt = 0
        prev = prices[i]

    return remain + buy_cnt * prices[-1]
    

init_cache = int(input())
prices = list(map(int,input().split()))

bnp = BNP(init_cache, prices)
timing = TIMING(init_cache, prices)

if bnp > timing:
    print("BNP")
elif timing > bnp:
    print("TIMING")
else:
    print("SAMESAME")

