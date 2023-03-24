def solution(n, k):
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n**(0.5)+1)):
            if n % i == 0:
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
