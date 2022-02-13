#선택 정렬 복잡도 O(N^2)
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스

    for j in range(i+1,len(array)): # 정렬되지 않은 array에서
        if array[min_index] > array[j]: # min_index 보다 작은 값이라면
            min_index = j # min_index는 j =>  정렬되지 않은 array에서 가장 작은 값 찾기
    array[i],array[i+1] = array[i+1], array[i] #현재 i와 정렬되지 않은 array에서 가장 작은 값 교환