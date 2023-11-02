#dip은 jiggle을 춘 다음이나 다다음, 또는 twirl을 추기 전에 출 수 있다.

def rule1(data):
    for i in range(len(data)):
        if data[i] == 'dip':
            #바로 직전이 jiggle 이거나 전전이 jiggle
            if data[max(0,i-1)] =='jiggle' or data[max(0,i-2)] == 'jiggle' or data[min(len(data)-1, i+1)] == 'twirl':
                continue
            data[i] = 'DIP'

# 모든 춤은 clap stomp clap으로 끝나야 한다.
def rule2(data):
    
    target = ["clap","stomp","clap"]
    if len(data) >= 3:
        for i in range(3):
            if target[i] != data[-3+i]:
                return False
        return True
    else:
        return False
    

# 만약 twirl을 췄다면, hop도 춰야한다.
def rule3(data):
    if 'twirl' in data:
        if 'hop' in data:
            return True
        return False 
    else:
        return True

# jiggle로 춤을 시작할 수 없다.
def rule4(data):
    if data[0] == 'jiggle':
        return False
    
    return True
        

# 반드시 dip을 춰야 한다.
def rule5(data):
    if 'dip' not in data:
        return False
    return True 

while True:
    try:
        n = list(input().split())
        rules = [False]*5
        
        if rule5(n):
            rules[4] = True
        if rule1(n):
            rules[0] = True
        if rule2(n):
            rules[1] = True
        if rule3(n):
            rules[2] = True
        if rule4(n):
            rules[3] = True
        
        origin = " ".join(n)
        if all(rules):
            print(f'form ok: {origin}')
        else:
            
            cnt = []
            for i in range(len(rules)):
                if not rules[i]:
                    cnt.append(i)
            
            if len(cnt) == 1:
                print(f'form error {cnt[0]+1}: {origin}')
            else:
                error_message = ['form errors ']

                for i in range(len(cnt)):
                    if i == 0:
                        pass
                    elif i == len(cnt) - 1:
                        error_message.append(" and ")
                    else:
                        error_message.append(", ")
                        
                    error_message.append(str(cnt[i]+1))
                error_message.append(": ")
                error_message.append(origin)
                print("".join(error_message))

    except EOFError:
        break
