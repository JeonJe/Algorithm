# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # Implement your solution here
    pass
    def check(mid):
        if X+D*mid >= Y:
            return True
        return False
    
    #한 번의 점프로 가는 경우도 고려해야하기 때문에 left는 0 
    left = 0
    right = 1000000001
    #점프가 필요하지 않을 경우도 생각해줘야함
    if X == Y:
        return 0 

    while left + 1 < right:
        mid = (left+right)//2

        if check(mid):
            right = mid
        else:
            left = mid
    return right