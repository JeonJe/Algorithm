from collections import Counter

N = int(input())


cnt=0
#한수 확인 범위 1부터 N까지
for i in range(1, N+1):
    result = []
    s = str(i)
    diff = 0
    #한자리 수이면 등차 수열 
    if len(s) < 2: 
        result.append(s)
       
    else:
        #두자리 이상 부터 각 자리 차이를 reulst에 넣음 
        for j in range(1, len(s)):
            diff = int(s[j-1]) - int(s[j])
            result.append(diff)
    #등차를 이루는 수가 1개이면 한수 
    if len(Counter(result)) == 1:
        cnt += 1
print(cnt)