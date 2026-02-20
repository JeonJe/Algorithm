import sys
sys.setrecursionlimit(10*6)
N = int(input())
bigest_digit = ['2','3','5','7']
smallest_digit = ['1','3','7','9']

def dfs(number):
    if len(number) == N:
        print(number)
        return
    for i in smallest_digit:
        if is_prime(number+i):
            dfs(number+i)


def is_prime(num):
    number = int(num)
    for i in range(2,int(number**(0.5))):
        if number % i == 0:
            return False
    return True 
       
ans = []

for n in bigest_digit:
    dfs(n)


