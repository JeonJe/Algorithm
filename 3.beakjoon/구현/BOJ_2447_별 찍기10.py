
def draw(n):
    if n == 1:
        return ['*']
    
    n = n // 3
    devide = draw(n)
    result = []

    for star in devide:
        result.append(star*3)
    for star in devide:
        result.append(star +' '*n + star)
    for star in devide:
        result.append(star*3)
    
    return result 


n = int(input())
print('\n'.join(draw(n)))