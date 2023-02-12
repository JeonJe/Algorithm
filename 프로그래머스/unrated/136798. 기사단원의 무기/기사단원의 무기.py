def common(n):
    arr = [ 0 for _ in range(n+1)]
    arr[1] = 1
    for i in range(2, n+1):
        temp = 0
        for j in range(1, int(i **(1/2)) + 1):
            if i % j == 0:
                temp +=1
                if j * j < i:
                    temp +=1

        arr[i] = temp
    return arr[1:]

def solution(number, limit, power):
    answer = 0
    arr= common(number)
    #기사단원의 넘버마다 약수의 개수를 구함 
    for a in arr:
        #필요한 공격력이 limit보다 크면 power 필요 
        if a > limit:            
            answer += power
        #아니라면 temp만큼 
        else:
            answer += a
    return answer
