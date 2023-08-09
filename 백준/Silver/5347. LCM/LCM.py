
# 최소공배수 = A*B / gcd(a,b)

n = int(input())
seq = [list(map(int,input().split())) for _ in range(n)]

def gcd(a,b):
    if a<b:
        a,b = b,a
    if a % b == 0:
        return b
    return gcd(a%b, b)

for a,b in seq:
    print(a*b//gcd(a,b))