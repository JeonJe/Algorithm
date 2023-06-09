import math

a = input()
b = input()

len_a = len(a)
len_b = len(b)
# def gcd(a,b):
#     if b == 0:
#         return a 
#     else:
#         return gcd(b, a%b)


print( 1 if a* len(b) == b*len(a) else 0)
    