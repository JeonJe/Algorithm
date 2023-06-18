
alpha = [0]*26

word = input()

for ch in word:
    
    alpha[ord(ch)-ord('a')] += 1

print(*alpha)