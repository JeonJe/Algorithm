

def quick_sort(arr, left, right):
    pl = left 
    pr = right 

    mid = (left+right) // 2

    pivot = arr[mid]

    while pl <= pr :
        while arr[pl] < pivot: pl += 1
        while arr[pr] > pivot: pr -= 1
        if pl <= pr:
            arr[pl], arr[pr] = arr[pr], arr[pl]
            pl+=1
            pr-=1

    if left < pr:
        quick_sort(arr,left, pr )
    if pl < right:
        quick_sort(arr, pl, right)
