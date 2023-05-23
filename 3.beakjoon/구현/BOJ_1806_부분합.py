import sys 

n , s = map(int,input().split())
seq = list(map(int,input().split()))

answer = sys.maxsize
left,right = 0,0
total = seq[0]

while( right < n and left <= right):

    #누적합이 s보다 작으면 right을 움직임
    if total < s :
        right+=1
        if right == n:
            break
        total += seq[right]
        # 
    #누적합이 s이상이면 left를 움직임
    elif total >= s :
        answer = min(answer,right-left+1)
        total -= seq[left]
        left+=1
    
print(answer if answer != sys.maxsize else 0)


