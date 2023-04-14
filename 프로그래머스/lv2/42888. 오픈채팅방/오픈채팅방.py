from collections import defaultdict 

def solution(record):
    answer = []
    temp = []
    dict = defaultdict(str)
    
    for i in range (len(record)):
        splited = record[i].split()
        action = splited[0]
        
        if action == "Enter":
            temp.append((action,splited[1]))
            dict[splited[1]] = splited[2]
        elif action == "Leave":
            temp.append((action,splited[1]))
        else:
            dict[splited[1]] = splited[2]
            
    for j in range(len(temp)):
        if temp[j][0] == "Enter":
            answer.append(f'{dict[temp[j][1]]}님이 들어왔습니다.')
        else:
            answer.append(f'{dict[temp[j][1]]}님이 나갔습니다.')
            
    return answer