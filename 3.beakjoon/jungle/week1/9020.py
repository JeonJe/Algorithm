import math
import sys
def eratos(n):

    arr = [False,False]+[True]*(n-1)
    primes = []

    for i in range(2, n+1):
        if arr[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                arr[j] = False
    
    return primes

T = int(input())
primes = eratos(100001)
for _ in range(T):
    n = int(input())
    
    mid_to_left = n // 2
    mid_to_right = n // 2
    
    while mid_to_left > 0:
        
        if mid_to_left in primes and mid_to_right in primes:
            print(mid_to_left, mid_to_right)
            break
        else:
            mid_to_left -= 1
            mid_to_right += 1
