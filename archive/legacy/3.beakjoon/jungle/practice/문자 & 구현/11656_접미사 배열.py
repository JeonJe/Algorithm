
input_string = input()

temp = []
for i in range(len(input_string)):
    temp.append(input_string[i:])

temp.sort()

for i in temp:
    print(i)