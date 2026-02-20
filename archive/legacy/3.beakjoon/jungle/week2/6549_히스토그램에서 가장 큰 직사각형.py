import sys 
import math

def get_mid_area(lo, hi, mid):
    pl = mid
    pr = mid
    height = histogram[mid]

    max_area = 1 * height

    while lo < pl and pr < hi:
        if histogram[pl - 1] < histogram[pr + 1]:
            pr += 1
            height = min(height, histogram[pr])
            
        else:
            pl -= 1
            height = min(height, histogram[pl])
        max_area = max(max_area, height * (pr - pl + 1))
        
    while pr < hi:
        pr += 1
        height = min(height, histogram[pr])
        max_area = max(max_area, height * (pr - pl + 1))
    while pl > lo :
            pl -= 1
            height = min(height, histogram[pl])
            max_area = max(max_area, height * (pr - pl + 1))
    return max_area 

def get_area(lo, hi):
    if lo == hi:
        return histogram[lo]

    mid = (lo + hi) // 2

    left_area = get_area(lo,mid)
    right_area = get_area(mid+1, hi)
    max_area = max(left_area, right_area)
    max_area = max(max_area, get_mid_area(lo,hi,mid))
    return max_area

while True:
    row = list(map(int,sys.stdin.readline().split()))
    n = row[0]
    
    if n == 0:
        break 
    histogram = row[1:]
    print(get_area(0,len(histogram)-1))


