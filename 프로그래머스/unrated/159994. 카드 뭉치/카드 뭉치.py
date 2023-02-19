def solution(cards1, cards2, goal):
    answer = "Yes"
    turn = 0
    p, p1, p2 = 0, 0, 0

    if goal[p] == cards1[p1]:
        turn = 1
    elif goal[p] == cards2[p2]:
        turn = 2
    else:
        return "No"

    #확인해야하는 단어가 남아 있을 경우 
    while p < len(goal):
        if turn == 1:
            if p1 >= len(cards1):
                return "No"
            
            if goal[p] != cards1[p1]:
                return "No"
            
            while p1 < len(cards1) and p < len(goal) and goal[p] == cards1[p1]:
                p+=1
                p1+=1
            turn = 2
        elif turn == 2:
            if p2 >= len(cards2):
                return "No"
            if goal[p] != cards2[p2]:
                return "No"
            while p2 < len(cards2) and p < len(goal) and goal[p] == cards2[p2]:
                p+=1
                p2+=1
            turn = 1

    return answer