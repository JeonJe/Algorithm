N = int(input())
arr = list(map(int,input().split()))

def is_prime(n):
    if n <= 1:
        return False
    for i in range( 2, int(n ** (1/2))+1):
        if n % i == 0:
            return False
    return True 

cnt = 0
for num in arr:  
    if is_prime(num):
        cnt+=1
print(cnt)