n = int(input())

prices = [int(input()) for _ in range(n)]
prices.sort(reverse=True)

total = 0
for i in range(0,len(prices),3):
    if len(prices[i:i+3]) == 3:
        total += sum(prices[i:i+2])
    else:
        total += sum(prices[i:i+3])


print(total)
