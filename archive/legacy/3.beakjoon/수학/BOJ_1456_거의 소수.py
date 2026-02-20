import sys 
input = sys.stdin.readline

def eratos():
    primes[0], primes[1] = False, False
    n = len(primes)
    for i in range(2, int(n**(1/2))+1):
        for j in range(2*i,n,i):
            primes[j] = False
    

A,B = map(int,input().split())
primes = [True] * (int(B ** (1/2))+1)
eratos()

answer = 0
for i in range(2, len(primes)):
    if primes[i]:
        temp = i * i 
        while True:
            if temp < A:
                temp *= i 
                continue
            if temp > B:
                break

            answer += 1
            temp *= i 
    
print(answer)