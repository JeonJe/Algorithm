import sys 

N = int(input())

arr = list(map(int,input().split()))
arr_cal = list(map(int,input().split()))
global res_min
global res_max 

res_min = sys.maxsize
res_max = -sys.maxsize

def dfs(depth, sum, arr_cal, arr):
    global res_min
    global res_max 

    if depth == N:
        res_max = max(res_max, sum)
        res_min = min(res_min, sum)
    else:
        
        if arr_cal[0] > 0:
            arr_cal[0] -= 1
            dfs(depth+1, sum+arr[depth],arr_cal,arr)
            arr_cal[0] += 1
        
        if arr_cal[1] > 0:
            arr_cal[1] -= 1
            dfs(depth+1, sum-arr[depth],arr_cal,arr)
            arr_cal[1] += 1
        
        if arr_cal[2] > 0:
            arr_cal[2] -= 1
            dfs(depth+1, sum*arr[depth],arr_cal,arr)
            arr_cal[2] += 1

        if arr_cal[3] > 0:
            arr_cal[3] -= 1
            if sum < 0 and arr[depth] > 0:
                 dfs(depth+1, -1*(-1*sum // arr[depth]),arr_cal,arr)
            else:
                 dfs(depth+1, sum//arr[depth],arr_cal,arr)
            arr_cal[3] += 1
        

dfs(1,arr[0],arr_cal,arr)
print(res_max)
print(res_min)