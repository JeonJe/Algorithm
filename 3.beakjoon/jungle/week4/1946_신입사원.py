import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    candi = []
    for i in range(N):
        paper, interview = map(int,input().split())
        candi.append((paper,interview))
    
    candi.sort()
    #서류 1등의 인터뷰 점수 
    max_interview = candi[0][1]
    cnt = 1
    for i in range(1,len(candi)):
        #서류 통과 점수 순으로 확인하였을 때 앞 지원자들의 최고 인터뷰 등수보다 더 작다면?
        #더 면접을 잘 본 것 -> 우선순위가 높다, 탈락하지 않는다. 최고 인터뷰 등수는 갱신 
        if candi[i][1] <= max_interview:
            max_interview = candi[i][1]
            cnt+=1

    print(cnt)