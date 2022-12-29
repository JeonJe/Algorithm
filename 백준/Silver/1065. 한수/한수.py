n = int(input())

cnt = 0

def check(x):
    digit = list(str(x))
    diff = 0
    if len(digit) <= 1:
        return True

    diff = int(digit[0]) - int(digit[1])
    for i in range(len(digit)-1):
        if diff != int(digit[i]) - int(digit[i+1]):
            return False
    return True


for i in range(1,n+1):
    if check(i):
        cnt += 1 
print(cnt)