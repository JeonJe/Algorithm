import sys 
input = sys.stdin.readline
n, m = map(int,input().split())

arr = {}

for i in range(n):
    name = input().rstrip()
    arr[name] = i+1

reverse_arr= dict(map(reversed,arr.items()))

for i in range(m):
    ins = input().rstrip()


    if ins.isalpha():
        print(arr[ins])
    else:
        print(reverse_arr[int(ins)])
