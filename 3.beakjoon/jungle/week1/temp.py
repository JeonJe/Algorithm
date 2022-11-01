
def kmp_match(txt : str, pat: str) -> int:
    #text를 따라가는 커서
    pt = 1
    #pat를 따라가는 커서
    pp = 0
    #건너뛰기 표
    skip = [0] * (len(pat) + 1) 

    #건너뛰기 표 생성
    skip[pt] = 0 
    while pt != len(pat):
        if pat[pt] == pat[pp]:
            pt += 1
            pp +=  1
            skip[pt] = pp
        elif pp == 0:
            pt += 1
            skip[pt] = pp
        else:
            pp = skip[pp]

    #문자열 검색하기
    pt = pp = 0
    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        elif pp == 0:
            pt += 1
        else:
            pp = skip[pp]
    
    return pt - pp if pp == len(pat) else -1 


A = "ABCDEFFFESGEAW"
B = "FESG"

print(kmp_match(A,B))

