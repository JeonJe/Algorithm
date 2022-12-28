
recs = [ list(map(int,input().split())) for _ in range(4) ]
area = [ [0]* 101 for _ in range(101) ]

for i in range(len(recs)):
    left_x, left_y, right_x, right_y  = recs[i][0], recs[i][1],recs[i][2],recs[i][3]
    for i in range(left_y,right_y):
        for j in range(left_x, right_x):
            area[i][j] = 1
    
sum = 0
for i in range(101):
    for j in range(101):
        if area[i][j] == 1:
            sum+=1

print(sum)