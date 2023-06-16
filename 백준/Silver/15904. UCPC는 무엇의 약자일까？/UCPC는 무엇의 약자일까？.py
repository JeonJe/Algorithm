seq = input()
target = "UCPC" 

j = 0
for i in range(len(seq)):
    if seq[i] == target[j]:
        j += 1
    if j == len(target):
        break

print("I love UCPC" if j == len(target) else "I hate UCPC" )

