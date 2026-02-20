import sys

# sys.stdin = open("input.txt",'rt')  

N = int(input())

arr = list(map(int,input().split()))

left = 0 
right = N-1
#증가수열의 마지막 값을 담는 변수 last
last = -1
res = ""
temp  = []

while left<=right:
    #배열의 왼쪽 오른쪽 값 중, 만드려고하는 증가수열의 마지막 값보다 크다면 temp 리스트에 임시로담음
    if arr[left]> last:
        temp.append((arr[left],"L"))
    if arr[right]>last:
        temp.append((arr[right],"R"))  
    temp.sort()
    #왼쪽 오른쪽을 잘랐을 때, 모두 증가수열의 마지막 값보다 작다면 증가수열 끝
    if len(temp)==0:
        break
    else:
        #아니라면 왼쪽, 오른쪽 자른 값 중 더 작은 값을 가져오고 인덱스 이동
        res+=temp[0][1]
        last = temp[0][0]
        if temp[0][1] == "L":
            left+=1
        else:
            right-=1
    temp.clear()

print(len(res))
print(res)



