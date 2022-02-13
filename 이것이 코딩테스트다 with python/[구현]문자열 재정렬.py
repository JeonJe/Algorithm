
data = "AJKDLSI412K4JSJ9D"

data1 = []

sum = 0
for i in range(len(data)):
    if data[i].isdigit():
       sum+=int(data[i])
    else:
        data1.append(data[i])

data1.sort()
data1.append(sum)

for i in data1:
    print(i,end='')
