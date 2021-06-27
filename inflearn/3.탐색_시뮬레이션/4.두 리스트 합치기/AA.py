import sys

# sys.stdin = open("input.txt",'rt')

a= input()
a_list = list(map(int,input().split()))
b =  input()
b_list = list( map(int,input().split()) )

result = a_list+b_list
result.sort()
print(' '.join(map(str,result)))