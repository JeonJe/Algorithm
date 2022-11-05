import sys
A,B,C = map(int,sys.stdin.readline().split())

def my_pow(A,B,C):

    if B == 1:
        return A % C
    else:
        if B % 2 == 0:
            half = my_pow(A,(B // 2),C)
            return half * half % C
        else:
            half = my_pow(A,(B // 2),C)
            return A * half * half % C 
        

print(my_pow(A,B,C))

