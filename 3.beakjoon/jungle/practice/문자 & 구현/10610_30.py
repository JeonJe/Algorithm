ins = list(input())

ins.sort(reverse=True)
ins = int(''.join(ins))

if ins % 30 == 0:
    print(ins)
else:
    print(-1)

