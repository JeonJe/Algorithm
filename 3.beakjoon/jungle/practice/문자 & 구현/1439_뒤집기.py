
data = list(map(int,input()))
i = 0

num_zero,num_one = 0,0

while i < len(data):
    if data[i] == 0:
        num_zero += 1
        while i < len(data) and data[i] == 0 :
            i += 1
        continue
    if data[i] == 1:
        num_one += 1
        while i < len(data) and data[i] == 1:
            i+= 1
        continue

print(min(num_zero, num_one))
