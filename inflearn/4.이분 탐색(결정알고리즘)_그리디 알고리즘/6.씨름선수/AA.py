
import sys
# sys.stdin = open("input.txt",'rt')

N = int(input())

arr = [ list(map(int,input().split())) for _ in range(N)]

arr.sort(key=lambda x : (-x[0],-x[1]))

res=[]
 
res.append((arr[0][0], arr[0][1]))

for i in range(1,N):
    #몸무게가 많이 나가는 순서대로 뽑는다.
    candiate_height, cadidate_weight = arr[i][0],arr[i][1]
    #남은지원자
    if  cadidate_weight > max(res,key=lambda x : x[1])[1]:
        res.append((candiate_height,cadidate_weight))
    #단 몸무게가 적게 나가도 

print(len(res))