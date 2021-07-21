
import sys
# sys.stdin = open("input.txt",'rt')

N = int(input())

arr = [ list(map(int,input().split())) for _ in range(N)]

#키가 큰 순서대로, 키가 같으면 몸무게가 무거운 순서대로 정렬
arr.sort(key=lambda x : (-x[0],-x[1]))

res=[]
 
 #가장 키가 큰 지원자는 선발
res.append((arr[0][0], arr[0][1]))

for i in range(1,N):
    #각 지원자들의 키와 몸무게를 가져온다.
    candiate_height, cadidate_weight = arr[i][0],arr[i][1]
    
    #현재 지원자와 선발된 지원자의 몸무게를 비교하여 
    # 현재 지원자의 몸무게가 선발된 지원자들 중 가장 무거운 지원자 보다 무거우면 선발
    
    if  cadidate_weight > max(res,key=lambda x : x[1])[1]:
        res.append((candiate_height,cadidate_weight))
    

print(len(res))