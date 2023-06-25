from decimal import Decimal, ROUND_HALF_UP

def custom_round(value, digits):
    rounded = Decimal(value).quantize(Decimal('0.' + '0' * digits), rounding=ROUND_HALF_UP)
    return float(rounded)

t = int(input())

for _ in range(t):
    seq = list(map(int,input().split()[1:]))
    avg = sum(seq) / len(seq)
    
    cnt = 0
    for s in seq:
        if s > avg:
            cnt += 1

    result = custom_round(cnt / len(seq) * 100, 3)
    print(f'{result:.3f}%')


    
    