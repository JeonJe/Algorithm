
def check(enemy,n,k):
   
    if k >= len(enemy):
        return True
    
    for i in range(k):
        enemy[i] = 0

    #0~k-1은 무적권을 사용 (0부터 시작이기 때문에)
    if sum(enemy) <= n:
        return True
    else:
        return False



def solution(n, k, enemy):
    enemy.sort(reverse=True)
    

    left = 0
    right = len(enemy) + 1

    while left + 1 < right:
        mid = (left+right) //2
        # mid라운드까지 버틸 수 있는지?
        if check(enemy[:mid],n,k):
            left = mid 
        else:
            right = mid 
    
    return left


n,k = 7,3
# enemy = [43,23,4,53,33,33,311]
enemy = [4, 2, 4, 5, 3, 3, 1]
print(solution(n,k,enemy))
