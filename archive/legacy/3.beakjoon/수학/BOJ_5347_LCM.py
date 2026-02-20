
# 최소공배수 = A*B / gcd(a,b)

n = int(input())
seq = [list(map(int,input().split())) for _ in range(n)]

def gcd(a,b):
    if a<b:
        a,b = b,a
    if b == 0:
        return a
    return gcd(b, a%b)

for a,b in seq:
    print(a*b//gcd(a,b))