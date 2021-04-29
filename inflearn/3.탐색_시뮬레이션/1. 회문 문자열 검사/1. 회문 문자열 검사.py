import sys

# sys.stdin = open("C:/Users/whsso/Desktop/AA/3.탐색_시뮬레이션/1. 회문 문자열 검사/input.txt","rt")

N = int(input())

for i in range(1,N+1):
    str = input()
    str = str.lower()
    length = len(str)
    pal =True
    for j in range (length//2):
        if str[j] != str[length-1-j]:
            pal=False
    if pal:
        print('#%d %s'%(i,'YES'))
    else:
        print('#%d %s'%(i,'NO'))