import sys

# sys.stdin = open("input.txt",'rt')

n = int(input())
arr = [ [ 0 for col in range(n)]  for row in range(n)]

for i in range(n):
    arr[i] = list(map(int,input().split()))

left = n // 2 
right = n // 2
mid = n //2

tot = 0
for i in range(n):
    for j in range(left,right+1):
            tot+=arr[i][j]
            
    if i < mid:
        left-=1
        right+=1
    else:
        left+=1
        right-=1

print(tot)