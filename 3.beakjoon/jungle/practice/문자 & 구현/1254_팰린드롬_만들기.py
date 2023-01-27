ins = list(input())

def is_palindrome(input):
    return input == input[::-1]
    
for i in range(len(ins)+1):
    temp = ins[:i]
    reverse_temp = temp[::-1]
    target = ins+reverse_temp
    if is_palindrome(target):
        print(len(target))
        break