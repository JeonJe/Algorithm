def roundTraditional(val, digits):
    return round(val+10**(-len(str(val))-1), digits)

t = int(input())

for _ in range(t):
    seq = list(map(int,input().split()[1:]))
    avg = sum(seq) / len(seq)
    
    cnt = 0
    for s in seq:
        if s > avg:
            cnt += 1

    result = roundTraditional(cnt / len(seq) * 100, 3)
    print(f'{result:.3f}%')


    
    