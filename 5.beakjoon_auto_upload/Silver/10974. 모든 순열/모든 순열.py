from itertools import permutations

n = int(input())
arr = [ i for i in range(1, n+1) ]
p = list(permutations(arr,n))
p.sort()
# p.sort(key=temp)

for x in p:
    print(*x)