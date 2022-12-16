n, l = map(int,input().split())

candi = [list(input()) for _ in range(n) ]

# standard = candi[0]

# -> digit 
for i in range(l):
    
    #row
    digit_diff  = 0
    for j in range(1,n):
        #각 자리별로 몇개의 문자가 다른지 확인 
        if candi[j][i] != candi[0][i]:
            digit_diff += 1

        #현재와 
        row_diff = 0
        for k in range(l):
            if candi[0][k] != candi[j][k]:
                row_diff +=1
        if row_diff > 2:
            print("CALL FRIEND")
            exit()

    if digit_diff == n-1 :
        candi[0][i] = candi[-1][i]
            


print(''.join(candi[0]))
   
