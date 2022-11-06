import sys
import heapq
n = int(input())

arr = list(map(int,sys.stdin.readline().split()))
arr.sort()

left = 0
right = len(arr) - 1

if n == 2:
    print(arr[left], arr[right])
    exit()

find_min = sys.maxsize 
mixed = 0
res = []
while left < right:
    cur_l = arr[left] 
    cur_r = arr[right] 
    mixed = cur_l + cur_r

    if mixed == 0:
        print(cur_l, cur_r)
        exit()

    #용액이 0과 얼마나 차이나는지 확인하고 제일 작다면 갱신 
    if abs(mixed) < find_min:
        find_min = abs(mixed)
        res = [cur_l, cur_r]

    if mixed < 0:
        left += 1
    else:
        right-=1

    
print(res[0], res[1])

        


