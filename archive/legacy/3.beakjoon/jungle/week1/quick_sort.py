

from typing import MutableSequence
def qsort(arr : MutableSequence, left : int, right : int) -> None:
    pl = left 
    pr = right 
    x = arr[(left+right) // 2]

    print(f'arr[{left}] ~ arr[{right}] : ', *a[left : right + 1])
    while pl<= pr:
        while arr[pl] < x: pl += 1
        while arr[pr] > x : pr -= 1

        if pl <= pr:
            arr[pl], arr[pr] = arr[pr], arr[pl]
            pl += 1
            pr -= 1
    if left < pr:
        qsort(arr, left, pr)
    if pl < right:
        qsort(arr,pl, right )

def quick_sort(arr : MutableSequence) -> None:
    qsort(arr, 0, len(arr)-1)

if __name__== '__main__':
    arr = [ 5,8,4,2,6,1,3,9,7]
    quick_sort(arr)
    
    print(arr)
