import sys 
input = sys.stdin.readline
n = int(input())

origin = [input() for _ in range(n)]

a = sorted(origin)
d = sorted(origin,reverse=True)

increasing = True 
decreasing = True

for i in range(len(origin)):
    if origin[i] != a[i]:
        increasing = False
    if origin[i] != d[i]:
        decreasing = False
    if not increasing and not decreasing:
        break

if not increasing and not decreasing:
    print('NEITHER')
elif increasing:
    print('INCREASING')
elif decreasing:
    print('DECREASING')

