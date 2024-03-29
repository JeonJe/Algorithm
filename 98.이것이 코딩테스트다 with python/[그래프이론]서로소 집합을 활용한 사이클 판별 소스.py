<<<<<<< HEAD
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] =  find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v,e = map(int,input().split())
parent = [0] * (v+1) #부모 테이블 초기화

#부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i] = i

cycle = False

for i in range(e):
    a,b = map(int,input().split())
    #사이클이 발생한 경우 종료

    if find_parent(parent,a) == find_parent(parent,b):
        cycle = True
        break
    else: #사이클이 발생하지 않았다면 합집합 수행
        union_parent(parent,a,b)

if cycle:
    print("사이클이 발생")
else:
=======
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] =  find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v,e = map(int,input().split())
parent = [0] * (v+1) #부모 테이블 초기화

#부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i] = i

cycle = False

for i in range(e):
    a,b = map(int,input().split())
    #사이클이 발생한 경우 종료

    if find_parent(parent,a) == find_parent(parent,b):
        cycle = True
        break
    else: #사이클이 발생하지 않았다면 합집합 수행
        union_parent(parent,a,b)

if cycle:
    print("사이클이 발생")
else:
>>>>>>> 65f2ee7131e2912c03d2122a15fcc235b3105750
    print("사이클이 발생하지 않음")