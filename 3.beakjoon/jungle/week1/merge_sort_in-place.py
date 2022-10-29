def merge_sort(arr):           
    def _merge_sort(a,left,right):

            if left < right:
                mid = (left + right) // 2

                _merge_sort(a, left, mid)
                _merge_sort(a, mid+1, right)

                p = 0
                j = 0
                i = left
                k = left 

                #i,p 로 a의 left부터 temp[0]에 담음 
                while i <= mid:
                    temp[p] = a[i]
                    copy_left += 1
                    i += 1

                #i은 남은 left arr를 담기 위해 사용, 
                # 배열 a의 뒷 부분과 temp 를 배열 a 에 병합 
                while i  <= right and j < p:
                    if temp[j] <= a[i]:
                        a[k] = temp[j]
                        j+=1 
                    #위에서 옮긴 left 중 mid보다 큰 
                    else:
                        a[k] = a[i]
                        i+=1
                    k+=1

                #temp 배열의 나머지원소를 a에 복사 
                while j < p:
                    a[k] = temp[j]
                    k += 1
                    j += 1

                    


    n = len(arr)
    temp = [None] * n           # 작업용 배열을 생성
    _merge_sort(arr, 0, n - 1)    # 배열 전체를 병합 정렬
    del buff         