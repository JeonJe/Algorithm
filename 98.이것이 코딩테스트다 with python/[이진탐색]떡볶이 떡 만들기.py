<<<<<<< HEAD
N, M = map(int,input().split())

req = list(map(int,input().split()))

req.sort()

start = 0
end = max(req)

result = 0

while (start<= end):
    mid = (start+end)//2
    total = 0
    for x in req:
        if x > mid: #잘랐을 때의 떡의 양 계산
            total = total + x - mid

    #떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if total < M:
        end = mid - 1

    #떡의 양이 충복한 경우 덜 자르기(오른쪽 부분 탐색)
    else:
        result = mid #최대한 덜 잘랐을 때가 정답이므로 여기에서 result에 기록
        start = mid + 1


=======
N, M = map(int,input().split())

req = list(map(int,input().split()))

req.sort()

start = 0
end = max(req)

result = 0

while (start<= end):
    mid = (start+end)//2
    total = 0
    for x in req:
        if x > mid: #잘랐을 때의 떡의 양 계산
            total = total + x - mid

    #떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if total < M:
        end = mid - 1

    #떡의 양이 충복한 경우 덜 자르기(오른쪽 부분 탐색)
    else:
        result = mid #최대한 덜 잘랐을 때가 정답이므로 여기에서 result에 기록
        start = mid + 1


>>>>>>> 65f2ee7131e2912c03d2122a15fcc235b3105750
