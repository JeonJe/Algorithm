def solution(price, money, count):
    answer = -1
    
    count_sum = (count * (count+1))//2
    total_price = price * count_sum
    
    if total_price > money:
        answer= total_price - money
    else:
        answer = 0
    return answer