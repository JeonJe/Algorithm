
s = []
for _ in range(9):
    s.append(int(input()))

s.sort()

for i in range(9):
    for j in range(9):
        if i == j:
            continue
            
            #s 중에서 i, j 가 가리키고 있는 인덱스를 제외한 나머지 값을 합산 
        temp = []
        for k in range(9):
            if k != i and k != j :
                temp.append(s[k])
        if sum(temp) == 100:
            temp.sort()
            for i in temp:
                print(i)


        