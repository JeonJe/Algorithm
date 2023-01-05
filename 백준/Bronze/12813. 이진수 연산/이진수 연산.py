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
print(bin(B^mask)[2:].zfill(n))