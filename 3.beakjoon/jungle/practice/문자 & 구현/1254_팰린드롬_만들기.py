ins = list(input())

reverse = ins[::-1]
res = []
for i in range(len(ins)):
    if ins[i] != reverse[i]:
        reverse.insert(0,ins[i])
    else:
        while