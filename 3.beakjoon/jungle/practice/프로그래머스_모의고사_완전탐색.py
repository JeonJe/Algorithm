from collections import defaultdict



def solution(answers):
    dict = defaultdict(list)

    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]

    cnt1,cnt2,cnt3 = 0,0,0
    
    for i, ans in enumerate(answers):
        if ans == pattern1[i%len(pattern1)]:
            cnt1 += 1
        if ans == pattern2[i%len(pattern2)]:
            cnt2 += 1
        if ans == pattern3[i%len(pattern3)]:
            cnt3 += 1
    
    dict[cnt1].append(1)
    dict[cnt2].append(2)
    dict[cnt3].append(3)

    sorting = sorted(dict.items(), reverse=True)
    return sorting[0][1]

answers = [1,2,3,2,4,2]
print(solution((answers)))