def solution(brown, yellow):
    answer = []

    total_area = brown + yellow
    for i in range(1,brown+1):
        
        if total_area % i == 0:
            x = i 
            y = total_area // x 
            # print(x , y)
            if x >=y :
                yellow_x = x-2
                yellow_y = y-2
                yellow_total = yellow_x * yellow_y
                if brown == total_area - yellow_total:
                    answer.append(x)
                    answer.append(y)
    return answer
    

    


brown = 50
yellow = 22

print(solution(brown,yellow))