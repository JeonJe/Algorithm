from collections import defaultdict 

def solution(elements):
    elements*=2
    sums = defaultdict(int)
    #idx 부터 시작
    for i in range(len(elements)//2):
    
        temp = 0
        #idx+j개
        for j in range(len(elements)//2):
            temp += elements[i+j]
            if temp not in sums:
                sums[temp]+=1
        
        
    return len(sums)
