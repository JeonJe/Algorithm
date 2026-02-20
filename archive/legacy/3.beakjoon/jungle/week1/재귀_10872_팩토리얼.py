N = int(input())

arr = [1,1] + [0] * (N-2)

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(N))

