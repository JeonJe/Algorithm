import sys
from collections import deque

# sys.stdin = open("input.txt",'rt')  

essential = list(input())
N = int(input())


for i in range(N):
    arr = list(input())
    #필수과목 리스트를 deque로 생성
    deq = deque(essential)

    #수업설계 과목을 확인하면서
    for x in arr:
        #필수 설계 과목인지 확인
        if x in deq:
            #필수 이수과목 순서대로 수강하지 않았으면? No
            if x != deq.popleft():
                print("#%d NO"%(i+1))
                break
    else:
        #필수 이수과목대로 모두 수강하였으면 YES
        if len(deq)==0:
             print("#%d YES"%(i+1))
        #모든 수업설계 과목을 비교하였고 필수 이수과목이 남아있으면 No
        else:
             print("#%d NO"%(i+1))


