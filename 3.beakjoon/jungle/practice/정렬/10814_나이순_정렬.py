
n = int(input())

infos = [input().split() for _ in range(n)]

for i in range(len(infos)):
    infos[i][0] = int(infos[i][0])
    infos[i].append(i)

infos.sort(key=lambda x: (x[0], x[2]))

for i in range(len(infos)):
    print(f'{int(infos[i][0])} {infos[i][1]}')