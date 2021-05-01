N,K = map(int,input().split())
arrA = list(map(int,input().split()))
arrB = list(map(int,input().split()))

arrA.sort()
arrB.sort(reverse=True)

for i in range(K): # 첫번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
    if arrA[i] < arrB[i]:
        arrA[i], arrB[i] = arrB[i],arrA[i]
    else:
        break


print(sum(arrA))

