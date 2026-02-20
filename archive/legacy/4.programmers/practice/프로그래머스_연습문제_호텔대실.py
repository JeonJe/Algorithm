from collections import defaultdict

def solution(book_time):
    dict = defaultdict(int)
    for start, end in book_time:
        s = int(start[:2])*60 + int(start[-2:])
        e = int(end[:2])*60 + int(end[-2:])
        for i in range(s, e+10):
            dict[i] += 1
    return max(dict.values())




book_time = [["09:10", "10:10"], ["10:20", "12:20"], ["12:30", "13:20"]]
print(solution(book_time))