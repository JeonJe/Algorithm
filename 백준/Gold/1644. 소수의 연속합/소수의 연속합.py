n = int(input())

if n == 1:
    print(0)
    exit(0)

primes = [True] * (n+1)
def eratos():
    primes[0], primes[1] = False, False

    for i in range(2,int(n**(1/2))+1):
        for j in range(2*i,n+1,i):
            primes[j] = False
    
eratos()
prime_list = [ i for i in range(n+1) if primes[i] == True]
left, right = 0,0
cnt = 0
cumul_sum = prime_list[left]

while left <= right:
    if cumul_sum == n:
        cnt += 1
        cumul_sum -= prime_list[left]
        left += 1
    elif cumul_sum > n:
        cumul_sum -= prime_list[left]
        left += 1
    else:
        right += 1
        if right == len(prime_list):
            break
        cumul_sum += prime_list[right]

print(cnt)