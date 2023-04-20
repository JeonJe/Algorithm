import math 

n,k = map(int,input().split())
arr = [ [0 for _ in range(7)] for _ in range(2)]

for i in range(n):
    gender, class_num = map(int,input().split())
    arr[gender][class_num] +=1

answer = 0
for i in range(1,7):
    for j in range(2):
        answer += math.ceil(arr[j][i]/k)

print(answer)