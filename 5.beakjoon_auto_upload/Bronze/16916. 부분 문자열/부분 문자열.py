import sys
input = sys.stdin.readline
text = input().rstrip()
pat = input().rstrip()


def kmp(text,pat):
    pt = 1
    pp = 0
    skip = [0] * (len(pat)+1)
    skip[pt] = 0 
    while  pt != len(pat):
        if pat[pp] == pat[pt]:
            pt+=1
            pp+=1
            skip[pt] = pp
        elif pp == 0:
            pt += 1
            skip[pt] = 0
        else:
            pp = skip[pp]
    
    pt = pp = 0

    while pt != len(text) and pp != len(pat):
        if text[pt] == pat[pp]:
            pt+=1
            pp+=1
        elif pp == 0:
            pt += 1
        else:
            pp = skip[pp]
    return 1 if pp == len(pat) else 0


print(kmp(text,pat))