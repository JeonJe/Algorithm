
import sys
# sys.stdin = open("input.txt",'rt')

def palindrome(str):
 
    rev_str = str[::-1]   

    if str == rev_str:
        return True
    else:
        return False


arr = [ (input().split()) for _ in range(7)]


cnt = 0
for i in range(7):
    for j in range(3):
        if palindrome(''.join(arr[i][j:j+5])):
            cnt+=1

for i in range(7):

    for j in range(3):
        col_str = ''
        for w in range(j,j+5):
            col_str += arr[w][i]
        
        if palindrome(col_str):
            cnt+=1
    
print(cnt)