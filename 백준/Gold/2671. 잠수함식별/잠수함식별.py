import re 
seq = input()

def is_want(seq):
    # 잠수함 패턴 (100~1~|01)~
    #100이 최소 1번 그리고 1이 최소 1번 나오거나 01이 나오는 패턴이 최소 한번은 나와야 한다.
    result = re.fullmatch('(100+1+|01)+', seq)
    return result

print('NOISE' if is_want(seq) is None else 'SUBMARINE')