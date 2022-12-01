import heapq
import sys

input = sys.stdin.readline

k  = int(input())
hq = []

lec_nums = [0] * (k+1) #강의 번호 
room_nums = [0] * (k+1) #강의실 번호 

for _ in range(k):
    recture_number, start, end = map(int,input().split())
    heapq.heappush(hq,(start,end,recture_number))



for i in range(1,k+1):
    cur_lec = heapq.heappop(hq)

    for j in range(1,k+1):
        #j번째 강의실이 강의가 끝나 비어지기 시작하는 시간이 현재 강의 시작시간보다 작으면
        #강의 넣기 
        if room_nums[j] <= cur_lec[0]:
            room_nums[j] = cur_lec[1]
            lec_nums[cur_lec[2]] = j
            break

cnt = 0
for i in range(1,k+1):
    if room_nums[i] != 0:
        cnt+=1
print(cnt)

for i in range(1,k+1):
    print(lec_nums[i])

