import sys
input = sys.stdin.readline
n, m = map(int,input().split())


def insert_trie(trie, word):
    for idx, char in enumerate(word):
        if char in trie:
            pass
        else:
            trie[char] = [{}, idx == len(word) - 1]
        trie, _ = trie[char]

def check_trie(trie, word):
    for idx, char in enumerate(word):
        if char in trie:
            if trie[char][1] or idx == len(word) - 1:
              return True  
        else:
            return False
        trie, _ = trie[char]
    return False 
trie = {}

for _ in range(n):
    s = input().rstrip()
    insert_trie(trie, s)

cnt = 0
for _ in range(m):
    s = input().rstrip()
    if check_trie(trie, s):
      cnt += 1
        
print(cnt)