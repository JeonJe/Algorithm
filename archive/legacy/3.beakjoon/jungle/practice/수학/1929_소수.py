M, N = map(int,input().split())

def eratos():
    primes[0],primes[1] = False, False

    for i in range(2, int(N**(1/2)+1)):
        for j in range(2*i,N+1,i):
            primes[j] = False

primes = [True]*(N+1)
eratos()

for i in range(M,N+1):
    if primes[i]:
        print(i)
