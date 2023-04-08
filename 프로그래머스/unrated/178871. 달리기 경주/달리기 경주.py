from collections import defaultdict 
def solution(players, callings):
    answer = []
    #key : 이름, value : 순위
    name = defaultdict(int)
    #key : 순위, value : 이름
    rank = defaultdict(str)
    
    for idx, players in enumerate(players):
        rank[idx] = players
        name[players] = idx
    
    for player in callings:
        
        #현재 플레이어가 몇 순위인지 
        player_rank = name[player]
        
        #추월할 사람이 있다면?
        if player_rank > 0:
            #앞에 사람과 이름 변동 
            name[player], name[rank[player_rank-1]] = name[rank[player_rank-1]], name[player]
            #앞에 사람과 순위 변동
            rank[player_rank], rank[player_rank-1] = rank[player_rank-1], rank[player_rank]
    for _, value in rank.items():
        answer.append(value)
    return answer