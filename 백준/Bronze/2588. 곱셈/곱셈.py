from re import A, T
import sys


f = int(sys.stdin.readline())
s = str(sys.stdin.readline())

a = f * int(s[2])
b = f * int(s[1])
c = f * int(s[0])
d = f * int(s)

print(a,b,c,d,sep='\n')
