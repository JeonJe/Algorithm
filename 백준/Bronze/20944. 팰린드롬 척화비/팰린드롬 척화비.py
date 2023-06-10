
n = int(input())

def is_palindrome(data):
    return data == data[::-1]

def is_sumi(data):
    mid = len(data) // 2
    if len(data) == 1:
        return True

    return data[:mid] == data[-mid:]
    

#길이가 N인 수미상관이면서 팰린드롬 문자열 
print("a"*n)


