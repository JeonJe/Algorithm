def solution(n):
    temp = ''
    
    while n >= 3:
        temp += str(n % 3)
        n //= 3
    temp += str(n)
    
    return int(temp,3)

n = 45 

print(solution(n))