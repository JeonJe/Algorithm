
# 유클리드 호제법 
# **2개의 자연수 a,b에 대해서 a를 b로 나눈 나머지를 r이라 하면
# (단 a>b) a와 b의 최대 공약수는 b와 r의 최대 공약수와 같다.**
# r = x % y 
# **이 성질에 따라 b를 r로 나눈 나머지 r0를 구하고, 
# 다시 r을 r0으로 나눈 나머지를 구하는 과정을 반복하여 
# 나머지가 0이 되었을 때 나누는 수가 a와 b의 최대 공약수이다.**
def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

a, b = map(int,input().split())

_gcd = gcd(a,b)
_lcm = (a*b) // _gcd 

print(_gcd)
print(_lcm)

