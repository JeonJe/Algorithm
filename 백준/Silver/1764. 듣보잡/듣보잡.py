
A,B = map(int,input().split())

list_a = [ input() for _ in range(A) ]
list_b = [ input() for _ in range(B) ]

set_a = set(list_a)
set_b = set(list_b)

#A와 B에 둘다 포함
intersec = list(set(set_a & set_b))
intersec.sort()

print(len(intersec))

for v in intersec:
    print(v)