from collections import defaultdict 

def solution(record):
    answer = []
    dict = defaultdict(str)
    actions = []
    ids = []
    
    for i in range (len(record)):
        splited = record[i].split()
        action = splited[0]
        
        if action == "Enter":
            actions.append(action)
            ids.append(splited[1])  
            dict[splited[1]] = splited[2]
        elif action == "Leave":
            actions.append(action)
            ids.append(splited[1])
        else:
            dict[splited[1]] = splited[2]
            
    for j in range(len(actions)):
        if actions[j] == "Enter":
            answer.append(f'{dict[ids[j]]}님이 들어왔습니다.')
        else:
            answer.append(f'{dict[ids[j]]}님이 나갔습니다.')
            
        
    return answer