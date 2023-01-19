position = { 1 : (0,0), 2: (0,1), 3 : (0,2), 4 : (1,0), 5 : (1,1), 6: (1,2), 7 : (2,0), 8 : (2,1), 9:(2,2),10:(3,0), 0:(3,1), 11:(3,2) }

def solution(numbers, hand):
    def check(left, right, target,hand):
        #1,4,7은 무조건 왼쪽 손, 3,6,9는 무조건 오른쪽 손   
        if target in [1,4,7,10]:
            return "left"
        elif target in [3,6,9,11]:
            return "right"
        else:
            left_x, left_y = position[left]
            right_x, right_y = position[right]
            target_x, target_y = position[target]
            left_dist = abs(left_x - target_x) + abs(left_y - target_y)
            right_dist = abs(right_x - target_x) + abs(right_y - target_y)
            if left_dist < right_dist:
                return "left"
            elif left_dist > right_dist:
                return "right"
            else:
                if hand == "left":
                    return "left"
                else:
                    return "right"
        
    answer = ''
    left,right = 10, 11
    
    #누를 숫자가 드러오면
    for i in range(len(numbers)):
        #해당 숫자와 왼손의 위치, 오른손의 위치의 거리차를 비교
        #어느손으로 업데이트 할 건지를 리턴 
        h = check(left,right,numbers[i],hand)
        #더 거리가 적은 쪽으로 해당 숫자를 누름 (위치 업데이트)
        if h == "left":
            left = numbers[i] 
            answer += 'L'
        else:
            right = numbers[i] 
            answer += 'R'

    #answer에 추가 
    return answer

