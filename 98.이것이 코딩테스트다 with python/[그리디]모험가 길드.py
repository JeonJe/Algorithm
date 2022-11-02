<<<<<<< HEAD
# N = map(int,input())
N =5

# arr = list(map(int,input().split()))
arr = [5,2,3,1,2,2]
arr.sort()

result, count = 0,0

for i in arr: #공포도가 낮은 사람부터 높은사람 순으로 확인
    count +=1  #공포도가 낮은 사람을 차례차례로 확인하기 때문에 카운터 변수 증가

    if count >= i : #만약 공포도가 낮은 사람이 현재 공포도보다 같거나 많이 구성되어있으면
        result+=1   #그룹하나 생성 완료
        count = 0   #그룹이 생성되었으므로 현재 그룹 구성원 수 0으로 초기화

print(result)
=======
# N = map(int,input())
N =5

# arr = list(map(int,input().split()))
arr = [5,2,3,1,2,2]
arr.sort()

result, count = 0,0

for i in arr: #공포도가 낮은 사람부터 높은사람 순으로 확인
    count +=1  #공포도가 낮은 사람을 차례차례로 확인하기 때문에 카운터 변수 증가

    if count >= i : #만약 공포도가 낮은 사람이 현재 공포도보다 같거나 많이 구성되어있으면
        result+=1   #그룹하나 생성 완료
        count = 0   #그룹이 생성되었으므로 현재 그룹 구성원 수 0으로 초기화

print(result)
>>>>>>> 65f2ee7131e2912c03d2122a15fcc235b3105750
