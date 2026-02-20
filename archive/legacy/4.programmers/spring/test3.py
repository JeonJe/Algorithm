def solution(queries):
    def is_pal(temp):
        if temp == temp[::-1]:
            return True
        return False

    #내 턴 때 팰린드롬을 만들 수 있는 지 체크,
    #있으면 해당 인덱스 리턴
    #없으면 -1 리턴
    def select(num_list):
        for i in range(len(num_list)):
            if num_list[i] != 0:
                num_list[i] -= 1
                if is_pal(num_list):
                    num_list[i] += 1
                    return i+1
                num_list[i] += 1
        return -1

    answer = []
    #라운드마다 배열이 공통 게임 배열이 주어짐
    for round in queries:
        check_list = round
        #한명이 이길 때까지 게임 진행 
        Flag = False
        who = 0
        while True:
            turn = select(check_list)
            #게임 종료 시 승자 확인        
            if turn >= 0:
                if who == 0:
                    answer.append(1)
                else:
                    answer.append(0)
                break
            #모두 확인했는데 팰린드롬을 만들지 못했다면 상대방이 
            #펠린드롬을 최대한 못 만들도록 수 선택
            for i in range(len(check_list)):
                if check_list[i] != 0:
                    check_list[i] -= 1
                    peer_turn = select(check_list)
                    if peer_turn == -1:
                        break
                        Flag = True
                    else:
                        check_list[i] += 1
            #아무거나 선택해도 상대방이 못만들면 가장 앞의 0을 
            if not Flag:
                for i in range(len(check_list)):
                    if check_list[i] != 0:
                        check_list[i] -= 1
                        break
            
            #다음사람에게 턴이동 
            who =  (who + 1) % 2
    return answer

queries = [[2,0],[3,1]]
print(solution(queries))

# def solution(queries):
#     def is_pal(temp):
#         if temp == temp[::-1]:
#             return True
#         return False

#     answer = []
#     #라운드마다 배열이 공통 게임 배열이 주어짐
#     for round in queries:
#         check_list = round
#         #한명이 이길 때까지 게임 진행 
#         Flag = False
#         who = 0
#         while True:
#             for i in range(len(check_list)):
#                 #0이 아닌 수를 하나씩 탐색해가며 1을뺴고 팰린드롬인지 확인
#                 if check_list[i] != 0:
#                     check_list[i] -= 1
#                     if is_pal(check_list):
#                         Flag = True
#                         break
#                     check_list[i] += 1
#             #게임 종료 시 승자 확인        
#             if Flag:
#                 if who == 0:
#                     answer.append(1)
#                 else:
#                     answer.append(0)
#                 break
#             #모두 확인했는데 팰린드롬을 만들지 못했다면 앞에서부터 하나 감소
#             #다음사람에게 턴이동 
#             for i in range(len(check_list)):
#                 #0이 아닌 수를 하나씩 탐색해가며 1을뺴고 팰린드롬인지 확인
#                 if check_list[i] != 0:
#                     check_list[i] -= 1
#                     break
#             who =  (who + 1) % 2
#     return answer