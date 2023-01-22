ins = list(input())
ins = list(map(int,ins))

ins.sort(reverse=True)
ins = map(str,ins)
print(''.join(ins))