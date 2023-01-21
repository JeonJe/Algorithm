def solution(arrayA, arrayB):
    def gcd(x,y):
        if y == 0:
            return x
        return gcd(y, x%y)
    res = 0

    #a 배열의 최대 공약수를 찾음
    gcd_a = arrayA[0]
    for a in arrayA[1:]:
        gcd_a = gcd(a, gcd_a)
    #b 배열의 최대 공약수를 찾음
    gcd_b = arrayB[0]
    for b in arrayB[1:]:
        gcd_b = gcd(b, gcd_b)
    
    #a의 최대공약수로 b가 나누어지는 지 확인
    for i in arrayB:
        if i % gcd_a == 0:
            break
    #모두 나눠지지 않는다면, res를 최대 공약수로 업데이트 (조건 만족)
    else:
        res = max(res,gcd_a)
    #b의 최대공약수로 a가 나누어지는 지 확인
    for i in arrayA:
        if i % gcd_b == 0:
            break
    else:
        res = max(res,gcd_b)

    return res