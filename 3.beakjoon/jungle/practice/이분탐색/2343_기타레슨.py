import sys

N, M = map(int,input().split())

videos = list(map(int,input().split()))

left = min(videos)-1
right = sys.maxsize

def check(time):
    temp = 0
    num_videos = 0
    for i in range(len(videos)):
        if temp + videos[i] <= time:
            if num_videos == 0:
                num_videos += 1
            temp += videos[i]
        else:
            temp = 0
            num_videos += 1
            if temp + videos[i] <= time:
                temp += videos[i]
            else:
                return False
    if num_videos <= M:
        return True
    else:
        return False

while left + 1 < right:
    mid = (left + right) // 2

    if check(mid):
        right = mid 
    else:
        left = mid 

print(right)