n = int(input())
seq = list(map(int,input().split()))
stack = []

for idx,value in enumerate(seq):
    while stack and stack[-1][0] < value:
        stack.pop()
    
    if not stack:
        print("0",end=' ')
    else:
        print(stack[-1][1]+1,end=' ')
    stack.append([value,idx])

