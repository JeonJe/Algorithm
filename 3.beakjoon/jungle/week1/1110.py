#주어진 수 
n = input()

if  int(n) < 10:
    n = '0' + n


cnt = 0 
old_num = n 

while True:
    cnt+=1
    sum_old = 0
    #각자리 수를 더함
    for i in range(len(old_num)):
        sum_old += int(old_num[i])
  
    #주어진 수의 가장 오른쪽 자리수와 앞에서 구한 합의 가장 오른쪽 자리수를 이어 붙인다
    new_num = old_num[-1] + str(sum_old)[-1]
    #처음 주어진 수와 새로만든 수가 같으면 그때까지 카운트한 값을 출력한다
    if n == new_num:
        print(cnt)
        break
    else:
        old_num = new_num
        

