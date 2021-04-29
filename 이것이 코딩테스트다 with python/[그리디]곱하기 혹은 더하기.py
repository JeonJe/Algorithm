
data = input()
result = int(data[0]) #처음 숫자, 만약 처음 숫자가 0이나 1이면 곱하기보다 더하기가 유리

for i in range(1,len(data)):
    if int(data[i]) <= 1 or result <= 1: #뒤에 연산하려는 수가 0이나 1이면 더하기가 유리, 결과값이 0이나 1이면 더하기가 유리
        result += int(data[i])
    else:
        result *= int(data[i])

print(result)
