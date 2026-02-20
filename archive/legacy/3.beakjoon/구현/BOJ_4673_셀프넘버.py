
check = [False] * 10036

def d(n):
    sum_n = n
    while n > 0:
        sum_n += n % 10
        n = n // 10
    return sum_n
    
for i in range(1,10001):
    dn = d(i)
    check[dn] = True

for i in range(1,10001):
    if not check[i]:
        print(i)
