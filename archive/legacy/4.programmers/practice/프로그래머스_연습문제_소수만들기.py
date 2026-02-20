from itertools import combinations

def eratos(primes):
    primes[0],primes[1] = False, False

    for i in range(2, int(len(primes) ** (1/2))+1):
        for j in range(2*i,len(primes),i):
            primes[j] = False
    return primes

def solution(nums):
    answer = 0
    primes = [True] * (max(nums) * 3)
    primes = eratos(primes)    
    permu = list(combinations(list(nums), 3))

    for p in permu:
        if primes[sum(p)]:
            answer+=1
            
    return len(answer)

nums = [1,2,7,6,4]
print(solution(nums))