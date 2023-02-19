def solution(cards1, cards2, goal):
    answer = "Yes"
    turn = 0
    p, p1, p2 = 0, 0, 0

    Flag = False
    while p < len(goal):
    
        while p1 < len(cards1) and p < len(goal) and goal[p] == cards1[p1]:
            p+=1
            p1+=1
            Flag = True
        
        while p2 < len(cards2) and p < len(goal) and goal[p] == cards2[p2]:
            p+=1
            p2+=1
            Flag = True
        
        if Flag:
            Flag = False
            continue
        else:
            return "No"
                

    return answer