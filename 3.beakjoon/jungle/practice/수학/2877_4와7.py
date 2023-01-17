from collections import deque

K = int(input())

print(bin(K+1)[3:].replace('0','4').replace('1','7'))



