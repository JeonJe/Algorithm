import math
    
def solution(n, k):
    answer = []
    seq = [i for i in range(1, n+1)]

    while n :
      
        temp = math.factorial(n) // n
        q = k // temp
        k = k % temp 

        if k == 0:
            answer.append(seq.pop(q-1))
        else:
            answer.append(seq.pop(q))
        n -= 1
    return answer
      

n = 3 
k = 5

print(solution(n,k))