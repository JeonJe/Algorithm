<<<<<<< HEAD
#시간 복잡도  O(N+K),  데이터의 개수를N, 데이터중 최대값의 크기를 K, 데이터의 크기가 한정되어 있고,
#데이터의 크기가 많이 중복되어 있을수록 유리하며 항상 사용할 수는 없다.

array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

count = [0] * (max(array)+1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)): # 카운트 배열의 인덱싱 확인
    for j in range(count[i]):   # 카운트 배열의 인덱싱에 나타난 숫자만큼 해당 숫자 반복됨
=======
#시간 복잡도  O(N+K),  데이터의 개수를N, 데이터중 최대값의 크기를 K, 데이터의 크기가 한정되어 있고,
#데이터의 크기가 많이 중복되어 있을수록 유리하며 항상 사용할 수는 없다.

array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

count = [0] * (max(array)+1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)): # 카운트 배열의 인덱싱 확인
    for j in range(count[i]):   # 카운트 배열의 인덱싱에 나타난 숫자만큼 해당 숫자 반복됨
>>>>>>> 65f2ee7131e2912c03d2122a15fcc235b3105750
        print(i, end=' ')