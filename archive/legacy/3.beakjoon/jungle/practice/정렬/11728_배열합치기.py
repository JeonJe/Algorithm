import sys 
input = sys.stdin.readline
N,M = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

res = []
i = 0 
j = 0
while i < len(A) and j < len(B):
    if A[i] < B[j]:
        print(A[i],end=' ')
        i += 1
    else:
        print(B[j],end=' ')
        j += 1

if i < len(A):
    while i < len(A):
        print(A[i],end=' ')
        i += 1
else:
    while j < len(B):
        print(B[j],end=' ')
        j += 1  
print()