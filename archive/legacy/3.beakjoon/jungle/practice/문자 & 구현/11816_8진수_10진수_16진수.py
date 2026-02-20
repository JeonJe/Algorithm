n = list(input())

if len(n) == 1:
    print(int(''.join(n)))
    exit()

if n[0] == '0':
    if n[1] == 'x':
        h = int(''.join(n[2:]),16)
        print(h)
    else:
        o =  int(''.join(n[1:]), 8)
        print(o)
else:
    print(int(''.join(n)))