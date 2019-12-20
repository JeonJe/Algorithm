# 두 문자열 s1 과 s2 를 붙여서 새 문자열을 만들려 합니다 . 이때 , 한 문자열의 끝과 다른 문자열의 시작
# 이 겹친다면 , 겹치는 부분은 한 번만 적습니다
# 두문자열 s1 과 s2 가 매개변수로 주어질 때 , s1 과 s2 를 붙여서 만들 수 있는 문자열 중 , 가장 짧은
# 문자열의 길이를 return 하도록 solution 함수를 완성해주세요

def findpattern(c1,c2):

    for i in range(1, min(len(c1),len(c2))):
        if c1[:i] == c2[i*-1:]:  # c2[i*-1:]는 뒤에서부터 인덱싱
            p_len = i
    return p_len

def solution(s1,s2):
    answer = 0
    p1 = findpattern(s1,s2)
    p2 = findpattern(s2,s1)
    print(len(s1),len(s2),max(p1,p2))
    answer = len(s1) + len(s2) - max(p1,p2)
    return answer

# def check(short,long,temp):
#     answer = -1
#     for i in range(len(short)+1):
#         if long[len(long)-i:len(long)] == short[:i] and len(short[:i])>0 :
#             answer=max(answer,len(short[:i]))
#             temp.append( len(long) + len(short) - answer )
#     return temp
# def solution(s1, s2):
#
#     print(len(s1),len(s2))
#     temp = []
#     temp = check(s1,s2,temp)
#     temp = check(s2,s1,temp)
#     if len(temp) > 0:
#         return min(temp)
#     else :
#         return len(s1)+len(s2)

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
s1 = "ababc"
s2 = "abcdab"
ret = solution(s1, s2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")