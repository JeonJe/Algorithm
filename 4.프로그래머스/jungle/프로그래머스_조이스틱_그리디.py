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
        
        # *2는 오고 가고,
        move = min(move, i*2+len(lists) - idx)
        move = min(move, (len(lists)-idx)*2+i)
    return answer+move
            

name = "JEROEN"
print(solution(name))