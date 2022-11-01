T = int(input())

Tn = [0] * 45

for i in range(1,45):
    Tn[i] = (i*(i+1))// 2

def check_eureka(l):
    for i in range(1,45):
        for j in range(1,45):
            for k in range(1,45):
                if Tn[i] + Tn[j] + Tn[k] == l:
                    return True
    return False

for _ in range(T):
    k = int(input())

    if check_eureka(k):
        print('1')
    else:
        print('0')