<<<<<<< HEAD

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
=======

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
>>>>>>> 65f2ee7131e2912c03d2122a15fcc235b3105750
