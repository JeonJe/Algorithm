import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
p_arr = list(map(int, input().split()))

parent = list(int(i) for i in range(n+1))

def find(a):
    if parent[a] == a: return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a==b: return
    if a<b: parent[b] = a
    else: parent[a] = b

for i in range(1, p_arr[0]):
    union(p_arr[i], p_arr[i+1])

party = []
for i in range(m):
    p = list(map(int, input().split()))
    party.append(p)
    if p[0]==1:
        #p[1] = parent[p[1]]
        continue
    else:
        for j in range(1, p[0]):
            union(p[j], p[j+1])

cnt = 0
if p_arr[0] == 0:
    cnt = m
else:
    for i in range(m):
        if find(party[i][1]) != find(p_arr[1]):
            cnt += 1

print(cnt)