T = int(input())

def plus(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return plus(n - 3) + plus(n - 2) + plus(n - 1)

while T > 0:
    n = int(input())
    print(plus(n))
    T -= 1