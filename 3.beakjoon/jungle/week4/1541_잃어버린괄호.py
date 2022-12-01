st = input()

minus = False
result = 0
temp = ""
for i in range (len(st)):
    if st[i] == '-' or st[i] == '+':
        if minus:
             result -= int(temp)
        else:
             result += int(temp)
        temp=""
        if st[i] == '-':
            minus = True
    else:
        temp += st[i]

if len(temp) > 0:
    if minus: result -= int(temp)
    else: result += int(temp)
print(result)

