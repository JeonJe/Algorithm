#시간복잡도 O(N^2), 대부분 정렬되어 있는 경우엔 O(N)의 복잡도를 가짐 

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
    for j in range(i,0,-1): # 인덱스 i부터 1까지 감소하며 반복하는 문법
        if array[j] < array[j - 1]: # 자기보다 큰 데이터가 있으면 스왑 (자리 찾아가기 위해)
            array[j],array[j-1] = array[j-1], array[j]
        else: #자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(array)