t = int(input())

def is_palindrome(word):
    return word == word[::-1]
for _ in range(t):
    answer = []
    n = int(input())
    seq = [ input() for _ in range(n) ]
    for i in range(n-1):
        for j in range(i+1,n):
            new_word = seq[i] + seq[j]
            new_word2 = seq[j] + seq[i]
            if is_palindrome(new_word):
                answer.append(new_word)
            if is_palindrome(new_word2):
                answer.append(new_word2)
    
    print (answer[0] if answer else '0')