import sys

cur, n = map(int, input().split())

charge, temp = 0, 0
#최저
recommend_plan = 299000
#최대금액
recommend_charge =  200000
prev_charge = 0
plans = [[29900, 300], [34900, 1000], [39900, 2000], [49900, 6000], [59900, 11000], [69900, sys.maxsize]]

for i in range(len(plans)):
    # temp는 추가 사용료 금액 
    if i == len(plans) - 1:
        temp = 0
    else:
        if n > plans[i][1]:
            temp = n - plans[i][1]
        else:
            temp = 0

        if temp < 5000 and temp * 20 > 25000:
            temp = 25000
        elif temp * 20 > 180000:
            temp = 180000
        else:
            temp *= 20

    if plans[i][0] == cur:
        prev_charge = plans[i][0] + temp
        continue

    charge = plans[i][0] + temp
    if charge < recommend_charge:
        recommend_charge = charge
        recommend_plan = plans[i][0]

print(recommend_plan, prev_charge, recommend_charge)