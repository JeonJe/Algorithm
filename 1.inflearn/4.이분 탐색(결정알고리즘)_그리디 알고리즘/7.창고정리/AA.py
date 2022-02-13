import sys

# sys.stdin = open("input.txt",'rt')

L = int(input())

arr =  list(map(int,input().split())) 
arr.sort(reverse=True)

M = int(input())

for _ in range(M):
   
    arr[0] -= 1
    arr[L-1] +=1
    arr.sort(reverse=True)

print(arr[0]-arr[L-1])
