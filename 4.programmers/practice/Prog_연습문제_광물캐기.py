pick_type = {
    0: "diamond",
    1: "iron",
    2: "stone",
}

def dfs(picks, minerals, select_pick, depth, tired):
    answer = []
    if depth >= len(minerals):
        return tired
    
    temp = minerals[depth:depth+5]
    cnt_dia = temp.count("diamond")
    cnt_iron = temp.count("iron")
    cnt_stone = len(temp) - cnt_dia - cnt_iron
    
    if select_pick == "diamond":
        tired += len(temp)
    elif select_pick == "iron":
        tired += 5*cnt_dia + len(temp)-cnt_dia
    else:        
        tired += 25*cnt_dia + 5*cnt_iron + cnt_stone
                
    if sum(picks) == 0:
        return tired
    
    for i in range(3):
        if picks[i] > 0:
            picks[i] -= 1
            answer.append(dfs(picks,minerals,pick_type[i],depth+5,tired))
            picks[i] += 1
    
    return min(answer)
        
                
                
def solution(picks, minerals):
    answer = []
    
    for i in range(3):
        if picks[i] > 0:
            picks[i] -= 1
            answer.append(dfs(picks,minerals,pick_type[i],0,0))
            picks[i] += 1
            
                
    return min(answer)

picks = [1, 3, 2]
minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
print(solution(picks,minerals))