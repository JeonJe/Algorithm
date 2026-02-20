
f = int(input())
s = int(input())
t = int(input())

mul = str(f*s*t)

for i in range(10):
    print(mul.count(str(i)))