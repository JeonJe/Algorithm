def solution(record):
    answer = []
    
    matrix = [ [] for _ in range(len(record)) ]

    for i in range(len(record)):
        name = record[i].split(':')[0]
        t1 = list(map(int,record[i].split(':')[1].split(',')))
        # print(list(name,t1,t2,t3,t4,t5))
        matrix[i].append((name,t1))
        print(matrix[i])



    #1 더많은 코스에서 완주

    #2 더 어려운 코스 완주 (가장 어려운 코스 비교)
    
    #3 메달의 개수 

    #4 완주시간 총합이 더 작음

    #5 이름 
    return answer


record = ["jack:9,10,13,9,15", "jerry:7,7,14,10,17", "jean:0,0,11,20,0", "alex:21,2,7,11,4", "kevin:8,4,5,0,0", "brown:3,5,16,3,18", "ted:0,8,0,0,8", "lala:0,12,0,7,9", "hue:17,16,8,6,10", "elsa:11,13,10,4,13"]
solution(record)