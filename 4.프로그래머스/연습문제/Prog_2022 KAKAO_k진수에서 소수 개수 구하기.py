


def solution(n, k):
    def is_prime(p):
        if p == 1:
            return False
        for j in range(2, p-1):
            if p % j == 0:
                return False
        return True
    def convert(n,k):
        rev = ''
        while n > 0:
            n, r = divmod(n,k)
            rev += str(r)
        return rev[::-1]
    
    answer = 0
    trans = convert(n,k)    
    arr = ' '.join(trans.split("0")).split()
    
    for a in arr:
        if is_prime(int(a)):
            answer += 1
    return answer


n = 437674
k = 3
print(solution(n,k))