import sys

# sys.stdin = open("input.txt",'rt')

#length길이로 N곡을 다 저장하려고 했을 때 DVD 개수 리턴 함수
def Count(length):
    #DVD에 개수
    cnt =1
    
    #DVD 노래 누적 시간
    sum = 0 
    
    for i in arr:
        #누적시간에 현재 수록곡 노래 시간을 더했을 때, 최소 노래길이를 초과할 경우
        if sum+i > length:
            #용량 초과로 곡 수록 불가
            cnt+=1
            #새로운 DVD 추가되야함
            sum = i
            #x노래가 새로운 DVD에 들어갔으므로 누적시간 업데이트'
        else:
            #DVD에 현재 수록곡 노래 시간을 더할 수 있을 경우
            sum+=i

    return cnt
        

#총 N개의 곡, M개의 DVD 개수 
N, M = map(int,input().split())

#라이브에서 부른 순서대로 부른곡의 길이 가 분단위로 주어짐
arr = list(map(int,input().split()))
#최소 크기를 결정해야함

#최소는 노래 길이가 1분, 최대는 라이브에서 부른 순서대로 다 담는 것

left = min(arr)
right = sum(arr)

while left <= right:
    #DVD한장의 용량
    target = (left + right) // 2

    #target길이만큼 노래의 길이를 수록할 수 있고, DVD의 총 개수가 M개보다 작을 경우
    if Count(target) <=  M:
        res = target
        #최소 용량의 크기를 줄이고 확인
        right = target - 1
    else:
        #최소 용량의 크기를 늘이고 확인
        left = target+1

print(res)