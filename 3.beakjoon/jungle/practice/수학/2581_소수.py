M = int(input())
N = int(input())
primes = [True]*(10001)

def eratos():
    primes[0] = False
    primes[1] = False
    
    for i in range(2, int(len(primes) ** (1/2)) + 1):
        for j in range(2*i,len(primes), i ):
            primes[j] = False
eratos()

sum = 0
min_prime = 0
for i in range(N,M-1,-1):
    if primes[i]:
        sum += i
        min_prime = i
if sum >= 2 and min_prime >= 2:

    print(sum)
    print(min_prime)
else:
    print(-1)
        
