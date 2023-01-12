def solution(t, p):
    t = list(t)
    p = list(p)
    cnt = 0
    for i in range(len(t)-len(p)+1):
        f = t[i:i+len(p)]
        if int(''.join(f)) <= int(''.join(p)):
           cnt += 1 
    return cnt
        