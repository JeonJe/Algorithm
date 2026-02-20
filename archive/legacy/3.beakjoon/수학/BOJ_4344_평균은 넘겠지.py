

t = int(input())

for _ in range(t):
    seq = list(map(int,input().split()[1:]))
    avg = sum(seq) / len(seq)
    
    cnt = 0
    for s in seq:
        if s > avg:
            cnt += 1

    percent = cnt / len(seq) * 100
    four = int(percent * (10**4)) % 10
    if four >= 5:
        percent = int(percent*(10**3)+1) / (10**3)
    
    print(f'{percent:.3f}%')

    