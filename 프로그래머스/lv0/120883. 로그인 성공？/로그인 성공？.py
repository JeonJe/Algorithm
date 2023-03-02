def solution(id_pw, db):
    answer = 'fail'
    for cur in db:
        if cur[0] == id_pw[0]:
            if cur[1] == id_pw[1]:
                answer="login"
            else:
                answer = "wrong pw"
        
    return answer