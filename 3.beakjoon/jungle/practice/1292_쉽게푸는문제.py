A,B = map(int,input().split())
arr = [0] * (1001)

#배열의 인덱스
j = 1
cur_num = 1
while j < len(arr):
    #현재 숫자
    k = cur_num
    
    for _ in range(cur_num):
        arr[j] = k
        j+=1
        if j == len(arr):
            break
        
    cur_num+=1
print(sum(arr[A:B+1]))