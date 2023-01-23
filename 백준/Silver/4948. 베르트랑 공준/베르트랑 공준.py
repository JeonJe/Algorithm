
def eratos(n):
    for i in range(2,int(n**(1/2))+1):
        for j in range(2*i, n, i):
            primes[j] = False


primes = [True]*(123457*2+1)
primes[0],primes[1] = False, False 

eratos(123457*2+1)

while True:
    n = int(input())

    if n == 0:
        break 

    res = 0
    for i in range(n+1,2*n+1):
        if primes[i]:
            res+=1
    print(res)