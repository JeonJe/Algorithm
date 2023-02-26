n = int(input())

info = [ int(input()) for _ in range(n) ]

primes = [True] * (10001)

def eratos():
    primes[0], primes[1] = False, False
    for i in range(2, int(len(primes) ** (1/2))):
        for j in range(2*i, len(primes), i):
            primes[j] = False

eratos()

for i in info:
    res = []
    temp = i
    for j in range(2,i):    
        if primes[j]:
            s = temp - j 
            if primes[s]:
                res.append((j,s))

    res.sort(key=lambda x : abs(x[0]-x[1]))
    print(*res[0])