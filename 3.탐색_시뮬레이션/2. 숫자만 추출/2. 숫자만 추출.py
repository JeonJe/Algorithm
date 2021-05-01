
import sys

sys.stdin = open("C:/Users/whsso/Desktop/AA/3.탐색_시뮬레이션/2. 숫자만 추출/input.txt",'rt')

str = list(input())
num = []

for s in str:
    if s.isdigit():
        num.append(s)
n = int(''.join(num))

cnt = 0
for i in range (1,n+1):
    if n % i ==0 :
        cnt+=1
print(n)
print(cnt)