def convert(n, base):
    temp = "0123456789ABCDEF"
    q, r = divmod(n, base)

    if q == 0:
        return temp[r]
    else:
        return convert(q, base) + temp[r]

def solution(n, t, m, p):
    answer = ''
    temp =''
    for i in range(m*t):
        temp += convert(i,n)
    
    while len(answer) < t:
        answer += temp[p-1]
        p += m

    return answer