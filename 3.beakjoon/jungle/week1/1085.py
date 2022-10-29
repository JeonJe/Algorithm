import sys

x, y, w, h = map(int, sys.stdin.readline().split())

r1 = min(w-x, x)
r2 = min(h-y, y)
print(min(r1,r2))