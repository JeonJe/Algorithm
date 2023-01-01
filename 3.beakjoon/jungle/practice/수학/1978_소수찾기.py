n = int(input())

info = list(map(int,input().split())) 

primes = [True] * (1001)
def eratos():
    primes[0], primes[1] = False, False
    for i in range(2, int(len(primes) ** (1/2))):
        for j in range(2*i, len(primes), i):
            primes[j] = False

eratos()

cnt = 0
for p in info:
    if primes[p]:
        cnt += 1
print(cnt)