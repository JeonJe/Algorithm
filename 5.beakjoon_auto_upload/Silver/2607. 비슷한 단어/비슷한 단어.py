from collections import defaultdict
dict = defaultdict(int)

n = int(input())
words = [ input() for _ in range(n) ]
cnt = 0

f = list(words[0])
for k in range(len(f)):
    dict[f[k]] += 1
    
for i in range(1,len(words)):
    
    s = list(words[i])
    if len(s) > len(f)+1 or len(s) < len(f) - 1:
        continue

    temp = dict.copy()        
    other_case_flag = False

    #기준단어와 다른단어 비교
    #기준단어에 포함된 단어들만 비교해서 몇개 더 많은지 적은지 확인 
    #기준단어에 아예 포함되 단어가 있으면 못만드는 단어 
    for j in range(len(s)):
            temp[s[j]] -= 1
        
    
    case = [0,0]
    
    for key,value in temp.items():
        #들어 있는 수 
        if value == 0:
            continue

        if value == 1:
            case[1] += 1
        elif value == -1:
            case[0] += 1
        else:
            other_case_flag = True 
            break
    
    if case[0] > 2 or case[1] > 2 :
        continue
    if sum(case) <= 2 and not other_case_flag:
        # print(s)
        cnt += 1

print(cnt)
        
    


