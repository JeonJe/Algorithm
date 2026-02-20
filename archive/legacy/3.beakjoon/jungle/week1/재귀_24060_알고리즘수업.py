import sys

global res 
global cnt 
res = 0
cnt = 0

N, K = map(int,input().split())
arr = list(map(int,sys.stdin.readline().split()))

def merge_sort(arr, left, right):
    global cnt 
    if left < right and cnt <= K:
        mid = (left + right) // 2
  
        merge_sort(arr, left, mid) #왼쪽 부분 정렬     
        merge_sort(arr, mid+1, right) #오른쪽 부분 정렬
        merge(arr, left, mid, right) #병합

#arr[p:q+1] 과 arr[q+1:r+1]은 이미 오름차순으로 정렬 
def merge(arr, left, mid,right):
    global res
    global cnt 
    i = left
    j = mid+1
    t = 0
    temp = []
    while i<=mid and j <=right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i+=1
        else:
            temp.append(arr[j])
            j+=1

    while i <= mid:
        temp.append(arr[i])
        i+=1
    while j <= right:
        temp.append(arr[j])
        j+=1

    i = left 
    t = 0
    while i <= right:
        arr[i] = temp[t]
        cnt+=1
        # 시간초과
        #    res.append(arr[i])

        if cnt == K:
            res = arr[i]
            break
            
        i+=1
        t+=1


merge_sort(arr,0,len(arr)-1)
print(res if res > 0 else -1)