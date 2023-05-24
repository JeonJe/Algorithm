
def solution(order):
    answer = 0
    n = max(order)

    sub_belt = []
    idx = 0
    for i in range(1,n+1):
        if i != order[idx]:
            sub_belt.append(i)

        else:
            idx += 1
            answer += 1
            
            while sub_belt:
                if sub_belt[-1] == order[idx]:
                    idx+=1
                    answer+=1
                    sub_belt.pop()
                else:
                    break
                
    return answer