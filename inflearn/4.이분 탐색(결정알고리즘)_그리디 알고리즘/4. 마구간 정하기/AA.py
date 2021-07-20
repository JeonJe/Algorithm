import sys

# sys.stdin = open("input.txt",'rt')


def Count(target):
    #모든 말들의 거리는 target 거리보다 크거나 같아야함

    #첫번째 마굿간에 말 한마리 배치
    cnt = 1
    prev_x= arr[0]


    for i in range(1,N):
        if arr[i]-prev_x>=target:
            prev_x=arr[i]
            cnt+=1
    return cnt

    #놓을 수 있는 말의 숫자 


#Input
#N개의 마구간, C마리 말
#N개 마구간에 대한 좌표위치 

N,C = map(int,input().split())
arr = [ int(input()) for _ in range(N)]
arr.sort()

#타겟은 가장 가까운 두 말의 최대 거리

#3개의 마무간이 있고, 2개의 말이 있을 경우 
#두말의 최대거리는 1부터  1,000,000,000 사이에 답이 있음

#가장 가까운 두말의 최대거리가 1일 수도있고
left = 1
right = max(arr)
res = 0
while left<=right:
    target = (left+right) //2

    #target이라는 최대거리로 놓을 수 있는 말이 C보다 많으면 
    if Count(target) >= C:
        res = target
        #최대 거리 증가 
        left = target+1
    else:
        right = target-1 

print(res)