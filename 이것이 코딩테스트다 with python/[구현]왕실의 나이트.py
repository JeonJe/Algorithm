<<<<<<< HEAD

i = input()
col = ord(i[0])-96
row = int(str(i[1]))
print(col,row)


dc = [-2,-2,-1,+1,+2,+2,-1,+1]
dr = [-1,+1,-2,-2,-1,+1,+2,+2]


count = 0

for i in range(8):
    ncol = col +dc[i]
    nrow = row +dr[i]

    if ncol < 1 or ncol >8 or nrow < 1 or nrow > 8:
        continue
    print(nrow,ncol)
    count+=1

=======

i = input()
col = ord(i[0])-96
row = int(str(i[1]))
print(col,row)


dc = [-2,-2,-1,+1,+2,+2,-1,+1]
dr = [-1,+1,-2,-2,-1,+1,+2,+2]


count = 0

for i in range(8):
    ncol = col +dc[i]
    nrow = row +dr[i]

    if ncol < 1 or ncol >8 or nrow < 1 or nrow > 8:
        continue
    print(nrow,ncol)
    count+=1

>>>>>>> 65f2ee7131e2912c03d2122a15fcc235b3105750
print(count)