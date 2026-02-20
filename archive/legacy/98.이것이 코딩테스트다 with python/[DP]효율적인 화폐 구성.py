<<<<<<< HEAD
n,m = map(int,input().split())
# m 원, n개 줄에는 화폐의 가치
array = []

for i in range(n):
    array.append(int(input()))

    #한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001]*(m+1)# m원 +1


#다이나믹 프로그래밍(Dynamic Programming)진행 보텀업
d[0] = 0

for i in range(n): #화계 종류 
    for j in range(array[i], m+1): #입력된 화폐 -> m원 +1원 까지
        if d[j-array[i]] != 10001: # i-k 원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j],d[j-array[i]]+1)

if d[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
=======
n,m = map(int,input().split())
# m 원, n개 줄에는 화폐의 가치
array = []

for i in range(n):
    array.append(int(input()))

    #한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001]*(m+1)# m원 +1


#다이나믹 프로그래밍(Dynamic Programming)진행 보텀업
d[0] = 0

for i in range(n): #화계 종류 
    for j in range(array[i], m+1): #입력된 화폐 -> m원 +1원 까지
        if d[j-array[i]] != 10001: # i-k 원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j],d[j-array[i]]+1)

if d[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
>>>>>>> 65f2ee7131e2912c03d2122a15fcc235b3105750
    print(d[m])