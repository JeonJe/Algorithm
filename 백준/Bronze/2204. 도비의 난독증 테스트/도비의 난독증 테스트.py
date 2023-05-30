while True:
    n = int(input())
    if n == 0:
        break
    else:
        seq = [ input() for _ in range(n) ]
        seq.sort(key=lambda x : x.lower() )
        print(seq[0])
        