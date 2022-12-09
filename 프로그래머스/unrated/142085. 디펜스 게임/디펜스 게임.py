
def check(enemy , n, k):
    if k >= len(enemy):
        return True 

    enemy.sort(reverse=True)
    
    for i in range(k):
        enemy[i] = 0
    
    if sum(enemy) <= n:
        return True
    else:
        return False
        
def solution(n, k, enemy):
    left = 0
    right = len(enemy) + 1

    while( left + 1 < right ):
        mid = (left + right) // 2
        if check(enemy[:mid], n, k):
            left = mid 
        else:
            right = mid
    
    return left