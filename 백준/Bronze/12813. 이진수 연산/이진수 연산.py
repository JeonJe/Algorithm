A = list(map(int,list(input())))
B = list(map(int,list(input())))
# # A & B
for i in range(len(A)):
    if A[i] and B[i]:
        print('1',end='')
    else:
        print('0',end='')
print()
#  A | B
for i in range(len(A)):
    if A[i] or B[i]:
        print('1',end='')
    else:
        print('0',end='')
print()
#  A ^ B
for i in range(len(A)):
    if  (A[i] != B[i]) and (A[i] or B[i]):
        print('1',end='')
    else:
        print('0',end='')
print()

#  ~A
for i in range(len(A)):
    if A[i]:
        print('0',end='')
    else:
        print('1',end='')
print()
#  ~B
for i in range(len(A)):
    if B[i]:
        print('0',end='')
    else:
        print('1',end='')
print()