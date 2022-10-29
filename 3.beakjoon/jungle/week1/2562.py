arr = []

for i in range(9):
    arr.append(int(input()))

arr = sorted(enumerate(arr), key=lambda x: -x[1])
print(arr[0][1],arr[0][0]+1, sep='\n')
