import itertools

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True

res = []
def solution(numbers):
    cnt = 0
  
    nums = list(map(int,numbers))

    for i in range(1,len(nums)+1):
        pCr = list(itertools.permutations(nums,i))
        
        for j in range(len(pCr)):
            target = int(''.join(map(str,pCr[j])))
            
            if is_prime(target):
                if target not in res:
                    print(target)
                    res.append(target)

    return len(res)

numbers = "17"
print(solution((numbers)))