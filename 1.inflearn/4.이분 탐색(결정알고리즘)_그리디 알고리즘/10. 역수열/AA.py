import sys

# sys.stdin = open("input.txt",'rt')  

N = int(input())

arr = list(map(int,input().split()))
res=[]

for i in range(N,0,-1):
    #앞에 큰수가 없으면 앞에다 붙이기
    res.insert(arr[i-1],i)

print(*res)