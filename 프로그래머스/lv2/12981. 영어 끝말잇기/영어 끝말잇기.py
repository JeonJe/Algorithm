from collections import defaultdict 

def solution(n, words):
    partis = [0]*n
    used = defaultdict(int)
    answer = [0,0]
    last = ''
    for i,word in enumerate(words):
        #몇번째 사람의 몇 번째 단어인지 체크 
        partis[i%n] += 1

        if (last != '' and list(last)[-1] != list(word)[0]) or word in used:
            answer[0] = (i%n)+1
            answer[1] = partis[i%n]
            return answer
        else:
            used[word] += 1
            last = word

    return answer