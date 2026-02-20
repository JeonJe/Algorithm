# A = list(map(int,list(input())))
# B = list(map(int,list(input())))
# # # A & B

# for i in range(len(A)):
#     if A[i] and B[i]:
#         print('1',end='')
#     else:
#         print('0',end='')
# print()
# #  A | B
# for i in range(len(A)):
#     if A[i] or B[i]:
#         print('1',end='')
#     else:
#         print('0',end='')
# print()
# #  A ^ B
# for i in range(len(A)):
#     if  (A[i] != B[i]) and (A[i] or B[i]):
#         print('1',end='')
#     else:
#         print('0',end='')
# print()

# #  ~A
# for i in range(len(A)):
#     if A[i]:
#         print('0',end='')
#     else:
#         print('1',end='')
# print()
# #  ~B
# for i in range(len(A)):
#     if B[i]:
#         print('0',end='')
#     else:
#         print('1',end='')
# print()
A = int(input(),2) 
B = int(input(),2)
n = 100000
mask = 2 ** n - 1

# 자리수를 맞추기 위해 zfill 사용
# 십진수끼리 & 비트연산자결 계산 결과 십진수 -> 이진수 변환 
print(bin(A&B)[2:].zfill(n))  
print(bin(A|B)[2:].zfill(n))
print(bin(A^B)[2:].zfill(n))
print(bin(A^mask)[2:].zfill(n))
print(bin(A^mask)[2:].zfill(n))