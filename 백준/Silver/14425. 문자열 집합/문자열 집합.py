
n, m = map(int,input().split())


def trie_insert(trie, word):
    for idx, char in enumerate(word):
        if char in trie:
            if trie[char][1] or idx == len(word) - 1:
                trie[char][1] = True
        else:
            trie[char] = [{}, idx == len(word) - 1]
        trie, _ = trie[char]

def trie_check(trie, word):
  for idx, char in enumerate(word):
    if char in trie:
        if trie[char][1] and idx == len(word) - 1:
            return True
        trie = trie[char][0]
    else:
        return False
  return False

trie = {}
for i in range(n):
    word = input()
    trie_insert(trie, word)

cnt = 0
for i in range(m):
    target = input()
    if trie_check(trie, target):
      cnt+=1

print(cnt)

