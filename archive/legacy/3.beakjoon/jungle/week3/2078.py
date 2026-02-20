
        #1,1
        #a,b
#a+b, b  /   a, a+b

A,B = map(int,input().split())
L,R = 0,0

while A!=1 or B!=1:
    #오른쪽 자식이 왼쪽 자식보다 클 때, 
    if A < B:
        R += 1
        #A쪽은 자식의 값으로 유지,B쪽은 B(큰값)-A(작은값) 으로 갱신
        B = B-A
    #왼쪽 자식이 오른쪽 자식보다 클 떄
    elif A > B:
        #B쪽은 자식의 값으로 유지,A쪽은 A(큰값)-B(작은값) 으로 갱신
        L += 1
        A = A-B

print(L,R)
