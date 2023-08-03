import sys
input = sys.stdin.readline
t = int(input())

def insert_trie(trie, word):
    for idx, char in enumerate(word):
        if char in trie:
            if trie[char][1] or idx == len(word) - 1:
                return False
        else:
            trie[char] = { }, idx == len(word) - 1
        trie, _ = trie[char]
    return True 

for _ in range(t):
    n = int(input())
    result = "YES"
    trie = { }
    for _ in range(n):
        s = input().rstrip()
        if not insert_trie(trie, s):
            result = "NO"
    print(result)