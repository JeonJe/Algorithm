import sys

# sys.stdin = open("input.txt",'rt')

nums = [ i for i in range (0,21)]

for i in range(10):
    N,M = map(int,input().split())

    temp = nums[N:M+1]
    temp=temp[::-1]
    nums[N:M+1] = temp


for i in range(1,21):
    print(nums[i],end=' ')
 
