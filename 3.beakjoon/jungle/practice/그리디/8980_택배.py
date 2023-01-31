nums_city, car_capa = map(int,input().split())

num_info = int(input())

info = [list(map(int,input().split())) for _ in range(num_info)]
#시작마을, 도착마을을 오름차순 정렬하면 반례가 생긴다. 
# 1 -> 5를 넣고 2->3, 3->4 은 못 넣는 경우 
info.sort(key=lambda x : (x[1]))
boxs = [car_capa]*(nums_city+1)

res = 0
for ft, to, weight in info:
    min_weight = car_capa
    #ft마을 -> 중간마을 -> to마을을 순회하며
    #어느 마을이 가장 택배를 적게 받을 수 있는지, 그 때의 양을 구한다
    for i in range(ft, to):
        min_weight = min(min_weight, boxs[i])
    #위에서 구한 제일 적은 택배량과 현재 배달하려고 하는 택배량 중 더 적은량으로 배달한다.
    min_weight = min(min_weight, weight)

    #위에서 정한 택배량만큼 차에 택배를 쌓아야 하므로 이제 마을에서는 해당량만큼은 받을 수 없다.
    for j in range(ft, to):
        boxs[j] -= min_weight
    
    res += min_weight

print(res)



