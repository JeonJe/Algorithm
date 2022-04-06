<<<<<<< HEAD
# data = input()
data = '10100000000001100000000011000000001000001111111'

zero,one = 0,0

if data[0]=='1':
    one+=1 # 1 개수 증가
else:
    zero+=1  #0 개수 증가

for i in range(len(data)-1):
    if data[i] != data[i+1]: # 연속된 숫자가 아닐 경우
        if data[i+1] == '1': #0에서 1로 바뀔 경우
            one+=1           #0
        else:                  #현재숫자가 1이면 1의 숫자 카운트
            zero+=1


print(min(zero,one))
=======
# data = input()
data = '10100000000001100000000011000000001000001111111'

zero,one = 0,0

if data[0]=='1':
    one+=1 # 1 개수 증가
else:
    zero+=1  #0 개수 증가

for i in range(len(data)-1):
    if data[i] != data[i+1]: # 연속된 숫자가 아닐 경우
        if data[i+1] == '1': #0에서 1로 바뀔 경우
            one+=1           #0
        else:                  #현재숫자가 1이면 1의 숫자 카운트
            zero+=1


print(min(zero,one))
>>>>>>> 65f2ee7131e2912c03d2122a15fcc235b3105750
