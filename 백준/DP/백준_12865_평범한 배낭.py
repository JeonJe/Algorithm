n, k = map(int, input().split())
#물건 종류, 무게 최대

#가치 DP
d = [[0]*(k+1) for _ in range(n+1)]

arr = [[0,0]]
for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        w = arr[i][0]
        v = arr[i][1]

        #새로 물건을 추가 할 수 없을 경우

        if j < w:
            #i번쨰 물건까지 살펴보았을 때 무게가 j인 배낭의 최대 가치는 i-1개 물건을 담은 경우의 가치와 동일
            d[i][j] = d[i-1][j]
        else:
            #j번째 물건까지 살펴보았을 때 무게가 i인 배낭의 최대 가치는
            # 물건 i-1개인 가치 또는 물건 i-1개이고 무게는 현재 물건을 담을 수 있으면서, 가치를 더해준 것 중 큰 것
            d[i][j] = max(d[i-1][j], d[i-1][j-w]+v)

print(d[n][k])