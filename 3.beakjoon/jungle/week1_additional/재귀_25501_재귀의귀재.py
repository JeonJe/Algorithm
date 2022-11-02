

global cnt 

def recursion(arr, left, right):
    
    global cnt
    cnt+=1
    #모두 검사하였을 때 펠린드롬
    if left >= right: return 1
    #펠린드롬이 아닐 때
    elif arr[left] != arr[right]: return 0
    #더 검사 할 게 남았을 때 
    else:
        return recursion(arr, left+1, right-1)

def isPalindrome(arr):
    return recursion(arr, 0, len(arr)-1)

n = int(input())

for _ in range(n):
    row = input()
    cnt = 0
    print(f'{isPalindrome(row)} {cnt}')
