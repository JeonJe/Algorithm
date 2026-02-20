def solution(lotteries):
    choice_list =[]
    for idx,lotterie_info in enumerate(lotteries):
        win, buy, amount = lotterie_info[0],lotterie_info[1],lotterie_info[2]

        #내가 이 로또를 산다면 당첨확률은 얼마?
        buy+=1
        #100퍼센트 당첨
        if win>=buy:
            choice_list.append((100,amount,idx+1))
        #무작위 확률에 따라 당첨
        else:
            choice_list.append((win/buy,amount,idx+1))
    # 확률이 높은순 -> 금액이 높은 순 
    choice_list.sort(key=lambda x : (-x[0],-x[1]))
    # 인덱스
    return choice_list[0][2]


lotteries = [[100,100,500],[1000,1000,100]]

print(solution((lotteries)))