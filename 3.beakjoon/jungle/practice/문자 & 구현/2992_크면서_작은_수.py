from itertools import permutations

n = input()
list_n = list(n)
permu = list(permutations(list_n,len(list_n)))

res = 1e9
int_n = int(n)

for value in permu:
    cur = int(''.join(value))
    if cur > int_n:
        res = min(res,cur)
print(res if res != 1e9 else 0)
