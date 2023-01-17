from itertools import combinations
import sys
N, M = map(int, input().split())

nums = list(map( int, input().split() ))
com_nums = list(combinations(nums,3))

diff = sys.maxsize
res_a,res_b,res_c = 0,0,0
for a,b,c in com_nums:
    if a+b+c <= M :
        temp = M - (a+b+c)
        if diff > temp:
            diff = temp 
            res_a = a
            res_b = b
            res_c = c 

        if diff == 0:
            print(a+b+c)
            exit()
print(res_a+res_b+res_c)
