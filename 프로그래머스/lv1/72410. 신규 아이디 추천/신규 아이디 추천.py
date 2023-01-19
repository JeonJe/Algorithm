import re

def solution(new_id):
    answer = '' 
    #step1
    new_id = new_id.lower()
    
    #step2
    answer = re.sub('[^0-9a-z\-_.]','',new_id)
 
    #step3
    answer = re.sub('\.+','.', answer)
    
    #step4
    # answer = answer.replace("^[.]|[.]&","")
    answer = re.sub('^[.]|[.]$','',answer)
    
    #step5
    if len(answer) == 0:
        answer = 'a'
    #step6
    if len(answer) >=16:
        answer = answer[:15]
        answer = re.sub('^[.]|[.]$','',answer)
    #step7
    if len(answer) <= 2:
        while len(answer) != 3:
            answer += answer[-1]
            
    return answer