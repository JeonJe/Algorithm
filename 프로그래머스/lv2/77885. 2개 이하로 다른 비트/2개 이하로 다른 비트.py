def check(x):
        #현재수가 짝수일 경우 
        if x % 2 == 0:
            return x+1
    
        #현재수가 홀수일 경우 
        binary = bin(x)[2:]
        binary = '0' + binary
        binary = binary[:binary.rindex('0')] + '10' + binary[binary.rindex('0') + 2:]
        return int(binary, 2)

def solution(numbers):
          
    answer = []  
    for i in range(len(numbers)):
        answer.append(check(numbers[i]))
        
    return answer