primes = [True] * (10001)

M = int(input())
N = int(input())

def eratos():
    primes[0],primes[1] = False,False

    for i in range(2,int(len(primes) ** (1/2))+1):
        for j in range(2*i,len(primes),i):
            primes[j] = False

sum_primes = 0
min_primes = 1e9
eratos()
for i in range(M,N+1):
    if primes[i]:
        sum_primes += i
        min_primes = min(min_primes,i)

if sum_primes == 0:
    print(-1)
else:
    print(sum_primes)
    print(min_primes)



