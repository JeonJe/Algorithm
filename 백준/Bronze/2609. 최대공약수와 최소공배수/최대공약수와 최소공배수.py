
def gcd(x,y):
    while y  :
        x,y = y, x%y

    return x 

def lcm(x,y):
    return x*y // gcd(x,y)

x, y = map(int, input().split())
print(gcd(x,y))
print(lcm(x,y))
