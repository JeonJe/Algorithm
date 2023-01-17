
import sys
N = int(input())
A = list(map(int,sys.stdin.readline().split()))
M = int(input())
B = list(map(int, sys.stdin.readline().split()))

def binary_search(arr, left, right, target):

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
    return -1


A.sort()
for i in B:
    res = binary_search(A, 0, len(A)-1, i)
    print(1 if res > -1 else 0)

