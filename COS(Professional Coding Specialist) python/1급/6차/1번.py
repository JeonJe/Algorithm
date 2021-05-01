# #문제1
# n x n 크기 격자 모양 정원에 칸마다 핀 꽃 또는 피지 않은 꽃을 심었습니다. 이 정원의 꽃이 모두 피는 데 며칠이 걸리는지 알고 싶습니다. 핀 꽃은 하루가 지나면 앞, 뒤, 양옆 네 방향에 있는 꽃을 피웁니다.
# 정원 크기 n과 현재 정원의 상태를 담은 2차원 리스트 garden이 주어졌을 때, 모든 꽃이 피는데 며칠이 걸리는지 return 하도록 solution 함수를 작성해주세요.
#
# ---
# #####매개변수 설명
# 정원 크기 n과 현재 정원 상태를 담은 2차원 리스트 garden이 solution 함수의 매개변수로 주어집니다.
# * 정원 크기 n은 1보다 크고 100 보다 작거나 같은 자연수입니다.
# * 정원 상태를 담은 2차원 리스트 garden의 원소는 0 또는 1 입니다.
# * 이미 핀 꽃은 1로 아직 피지 않은 꽃은 0으로 표현합니다.
# * 정원에 최소 꽃 한 개는 피어 있습니다.
#
# ---
# #####return 값 설명
# 꽃이 모두 피는데 며칠이 걸리는지 return 합니다.
#
# ---
# #####예시
#
# | n | garden                        	| return |
# |---|-----------------------------------|--------|
# | 3 | [[0, 0, 0], [0, 1, 0], [0, 0, 0]] | 2  	|
# | 2 | [[1, 1], [1, 1]]              	| 0  	|
#import math
import queue

Dx = [-1,1,0,0]
Dy = [0,0,-1,1]

def solution(n, garden):
    answer = 0
    q = queue.Queue() # 새로운 큐 생성
    for i in range (n):
        for j in range(n):
            if garden[i][j]==1:
                q.put((i,j,0))

    while q.empty() == False: # 꽃이 모두 필때 까지
        x,y,day = q.get() # 현재 격자 정보

        for i in range(4): # 현재 꽃이 네 방향으로 꽃을 피움
            nex_x = x + Dx[i]
            nex_y = y + Dy[i]
            nex_day = day +1
            # 격자 내 칸에 꽃이 피지 않았으면
            if(0<=nex_x<n and 0<=nex_y<n and garden[nex_y][nex_x]==0):
                garden[nex_y][nex_x] = 1
                q.put((nex_y,nex_x,nex_day))
                answer = nex_day

    return answer




#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
n1 = 3
garden1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
ret1 = solution(n1, garden1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

n2 = 2
garden2 = [[1, 1], [1, 1]]
ret2 = solution(n2, garden2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")