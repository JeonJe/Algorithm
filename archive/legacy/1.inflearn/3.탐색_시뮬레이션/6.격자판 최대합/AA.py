import sys

# sys.stdin = open("input.txt",'rt')

n = int(input())

def MaxSum(arr):
    rMax= -1
    cMax= -1
    leftSum, rightSum = 0,0
    for i in range(n):
        rowSum = 0
        colSum = 0
        leftSum += int(arr[i][i])
        for j in range(n):
            rowSum += int(arr[i][j])
            colSum += int(arr[j][i])
        if rowSum > rMax:
            rMax = rowSum
        if colSum > cMax:
            cMax = colSum
    for j in range(n-1,0,-1):
        rightSum += int(arr[j][n-j])

    return max(rMax,cMax,leftSum,rightSum)
 


arr = [ [ 0 for col in range(n)]  for row in range(n)]


for i in range(n):
    arr[i] = input().split()
   
Max = MaxSum(arr)
print(Max)


