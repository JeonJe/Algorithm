def check_prime_number(num):

    if num == 1: 
        return False
    
    for i in range(2,num):
        if num % i == 0:
            return False
    return True 

N = int(input())
arr = list(map(int,input().split()))

cnt = 0
for j in arr:
    if check_prime_number(j):
        
        cnt += 1
print(cnt)