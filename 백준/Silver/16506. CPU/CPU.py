N = int(input())

inst = {'ADD' : 0, 'SUB' : 1, 'MOV' : 2, \
        'AND' : 3, 'OR' : 4, 'NOT' : 5, 'MULT' : 6, \
        'LSFTL' : 7, 'LSFTR' : 8, 'ASFTR' : 9,\
        'RL' : 10, 'RR' : 11}

orders = []
for _ in range(N):
    orders.append(list(input().split()))

for op, rD, rA, rB in orders:
    bits = ''
    
    if op[-1]!='C':
        bits = str(bin(inst[op])[2:].zfill(4))
        bits+='00'
    else:
        bits = str(bin(inst[op[:-1]])[2:].zfill(4))
        bits+='10'
    
    # print((bin(int(rD))[2:].zfill(3)))
    bits += str(bin(int(rD))[2:].zfill(3))
    bits += str(bin(int(rA))[2:].zfill(3))
    
    if op[-1]!='C':
        bits += str(bin(int(rB))[2:].zfill(3))+'0'
    else:
        bits += str(bin(int(rB))[2:].zfill(4))

    print(bits)

    
    