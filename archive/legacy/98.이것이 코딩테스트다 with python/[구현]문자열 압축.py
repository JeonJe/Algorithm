<<<<<<< HEAD
def solution(s):
    answer = 0
    length = []  # 문자열을 짤랐을 때 결과 값을 가지고 있는 리스트
    result = ""  # 문자열을 짤랐을 때 결과 값

    if len(s) == 1:  # 문자열을 짜를 필요가 없음
        return 1
    ㅁ
    for cutPos in range(1, len(s) // 2 + 1):  # 절반이상 자르는건 무의미
        count = 1  # 아직 반복되는게 없으므로 1로 초기화
        temp = s[:cutPos]  # 첫 문자열부터 cutPos 단위로 짜름

        for i in range(cutPos, len(s), cutPos):  # cutPos부터 끝까지 3씩 증가
            if s[i:i + cutPos] == temp:  # cutPos 만큼씩 문자열 잘라서 앞에 짜른 문자열과 비교
                count += 1  # 같다면 증가
            else:
                if count == 1:
                    count = ""
                result += str(count) + temp  # 반복되는문자열이 없으면 그대로 사용
                temp = s[i:i + cutPos]  # 다음 문자열로 이동
                count = 1  # 카운트 초기화

        if count == 1:  # 자르고 마지막 남은 문자열을 그대로 붙임
            count = ""
        result += str(count) + temp

        length.append(len(result))
        result = ""

    return min(length)


input = "abcabcabcabcdededededede" #14
=======
def solution(s):
    answer = 0
    length = []  # 문자열을 짤랐을 때 결과 값을 가지고 있는 리스트
    result = ""  # 문자열을 짤랐을 때 결과 값

    if len(s) == 1:  # 문자열을 짜를 필요가 없음
        return 1
    ㅁ
    for cutPos in range(1, len(s) // 2 + 1):  # 절반이상 자르는건 무의미
        count = 1  # 아직 반복되는게 없으므로 1로 초기화
        temp = s[:cutPos]  # 첫 문자열부터 cutPos 단위로 짜름

        for i in range(cutPos, len(s), cutPos):  # cutPos부터 끝까지 3씩 증가
            if s[i:i + cutPos] == temp:  # cutPos 만큼씩 문자열 잘라서 앞에 짜른 문자열과 비교
                count += 1  # 같다면 증가
            else:
                if count == 1:
                    count = ""
                result += str(count) + temp  # 반복되는문자열이 없으면 그대로 사용
                temp = s[i:i + cutPos]  # 다음 문자열로 이동
                count = 1  # 카운트 초기화

        if count == 1:  # 자르고 마지막 남은 문자열을 그대로 붙임
            count = ""
        result += str(count) + temp

        length.append(len(result))
        result = ""

    return min(length)


input = "abcabcabcabcdededededede" #14
>>>>>>> 65f2ee7131e2912c03d2122a15fcc235b3105750
print(solution(input))