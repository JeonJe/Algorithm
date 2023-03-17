def solution(name):
    answer = 0 
    lists = [ min(ord(s)-ord('A'),ord('Z')-ord(s) + 1) for s in name]
    idx = 0
    move = len(name) - 1
    for i in range(len(lists)):
        #스틱 위, 아래 중 최소값을 answer에 삽입 (=이동)
        answer += lists[i]

        idx = i+1
        while(idx < len(lists) and lists[idx] == 0):
            idx+=1
        
     # 1. 원점을 기준으로 x까지 탐색하고, 다시 역방향으로 y를 탐색했을 때 거리
    # 2. 원점을 기준으로 역방향 y까지 탐색하고, 다시 정방향으로 X까지 탐색했을 때 이동거리
        move = min(move, i+len(lists)-idx+min(i,len(lists)-idx))
        
    return answer+move