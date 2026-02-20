from collections import defaultdict 
n = int(input())

enter_order = defaultdict(int)
for i in range(n):
    car_number = input()
    enter_order[car_number] = i


cnt = 0
out_order = []
for i in range(n):
    out_order.append( input())

for i in range(n-1):
    # 현재 차량보다 뒤에 있는 차량 중에
    for j in range(i+1,n):
        # 현재 차량보다 들어온 순번이 더 빠른(작은)) 차량이 있는 경우 현재 차량을 추월한 차량으로임
        if enter_order[out_order[i]] > enter_order[out_order[j]]:
            cnt+=1
            break

print(cnt)