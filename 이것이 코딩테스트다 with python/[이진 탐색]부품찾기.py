def binary_search(arr,target,start,end):
    while start <= end:
        mid = (start+end)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] >target:
            end = mid - 1
        else:
            start = mid+1
    return None

M = int(input())
stock = list(map(int,input().split()))

N = int(input())
req = list(map(int,input().split()))

stock.sort()

for i in req:
    if binary_search(stock,i,0,len(stock))==None:
        print("No", end=' ')
    else:
        print("Yes",end=' ')

n = int(input())
array = set(map(int,input().split()))
#가게에 있는 전체 부품 번호를 입력받아서 집합(set) wkfyguddp rlfhr
#단순히 특정한 데이터가 존재하는지 검사할 때 효과적

x = list(map(int,input().split()))
for i in x:
    #해당 부품이 존재하는 지 확인
    if i in array:
        print('yes',end=' ')
    else:
        print('no', end=' ')
