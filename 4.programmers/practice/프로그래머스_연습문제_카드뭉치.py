def solution(cards1, cards2, goal):
    answer = "Yes"
    turn = 0
    p, p1, p2 = 0, 0, 0

    if goal[p] in cards1:
        turn = 1
    elif goal[p] in cards2:
        turn = 2
    else:
        return "No"

    #확인해야하는 단어가 남아 있을 경우 
    while p < len(goal):
        if turn == 1:
            if goal[p] not in cards1:
                return "No"
            while cards1 and goal[p] in cards1:
                del cards1[cards1.index(goal[p])]
                p+=1
            turn = 2
        elif turn == 2:
            if goal[p] not in cards2:
                return "No"
            while cards2 and goal[p] in cards2:
                del cards2[cards2.index(goal[p])]
                p+=1
            turn = 1

    return answer

cards1 = ["i", "water", "drink"]
cards2 = ["want", "to"]
goal = 	["i", "want", "to", "drink", "water"]

print(solution(cards1, cards2, goal))