import sys

# sys.stdin = open("input.txt",'rt')

arr = [ i for i in range(21)]

for _ in range(10):
    a,b = map(int,input().split())
    for i in range( (b-a+1)//2):

        arr[a+i], arr[b-i] = arr[b-i], arr[a+i]

print(' '.join(map(str,arr[1:21])))
# arr.pop(0)

# for x in arr:
#     print(x, end=' ')
