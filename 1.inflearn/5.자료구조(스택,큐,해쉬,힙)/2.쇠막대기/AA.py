import sys

# sys.stdin = open("input.txt",'rt')

arr = input()
stack =[]
cnt = 0


for i in range(len(arr)):
    if arr[i] == "(":
        stack.append(arr[i])
        
    else:
        #레이저임, 계산해줘야함
        stack.pop()
        if arr[i-1] == "(":
            #앞에 있는 쇠막대기의 개수를 카운트
            cnt+=len(stack)
        else:
            #쇠막대기 하나가 끝났기 때문에 pop시켜야함

            cnt+=1

print(cnt)