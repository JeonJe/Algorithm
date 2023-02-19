from itertools import permutations

def eratos(primes):
    primes[0],primes[1] = False, False

    for i in range(2, int(len(primes) ** (1/2))+1):
        for j in range(2*i,len(primes),i):
            primes[j] = False
    return primes

def solution(nums):
    answer = []
    primes = [True] * (max(nums) * 3)
    primes = eratos(primes)    
    permu = list(permutations(list(nums), 3))

    for p in permu:
        
        if primes[sum(p)]:
            temp = []
            
            for i in p:
                temp.append(i)
            temp.sort()

            if temp not in answer:
                answer.append(temp)
            
    return len(answer)
