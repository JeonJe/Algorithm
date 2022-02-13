
T = int(input())

for _ in range(T):
    N = int(input())  # 트리를 구성하는 노드의 수
    parent = [0] * (N+1)

    for _ in range(N-1):
        A,B = map(int,input().split())
        parent[B] = A

    target_1,target_2 = map(int,input().split())
    target_1_list = [target_1]
    target_2_list = [target_2]

    while target_1:
        target_1_list.append(parent[target_1])
        target_1 = parent[target_1]

    while target_2:
        target_2_list.append(parent[target_2])
        target_2 = parent[target_2]

    for i in target_1_list:
        if i in target_2_list:
            print(i)
            break