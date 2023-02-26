
st = list(input())
bomb = list(input())

bomb_len = len(bomb)
stack = []

#입력 문자열을 왼쪽에서 오른쪽으로 확인하면서
for c in st:
    #확인한 char를 stack에 삽입
    stack.append(c)
    #현재 확인중인 문자열이 폭탄의 가장 뒷 문자와 같고
    #스택에 쌓인 문자열 중 폭발 문자열만큼 비교하였을 때 폭발 문자열과 같으면 스택에서 삭제 
    if c == bomb[-1] and "".join(stack[-bomb_len:]) == "".join(bomb):
        del stack[-bomb_len:]

print( "".join(stack) if len(stack) > 0 else "FRULA")