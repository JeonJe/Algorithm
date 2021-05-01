
# 핸드폰 화면에 문구를 출력해주는 전광판 어플이 있습니다 . 문구는 "happy birthday" 로 설정하였습니
# 다 . 전광판 어플은 다음과 같은 규칙으로 화면에 문구를 출력해 줍니다
# * 어플은 화면에 14 자 문구를 출력합니다
# * 문구는 1 초에 왼쪽으로 한 칸씩 움직입니다
# * 문구 이외의 부분은 로 표시됩니다
# * 어플은 설정한 문구를 화면에 반복해 출력합니다 .
# * 어플은 문구가 다 지나가면 설정한 문구를 반복해 보여줍니다
#
# 문구를 담은 문자열 phrases 와 초를 담은 second 가 매개변수로 주어질 때 , 화면에 보이는 문자열을
# 출력하도록 solution 함수를 작성해 주세요
# 단 , 는 공백을 나타냅니다
# def solution(phrases, second):
#     # 여기에 코드를 작성해주세요.
#     cut1 = second % 28
#     str = ""
#
#     if cut1<= 14:
#         for i in range(len(phrases)-cut1):
#             str += '_'
#         for i in range(cut1):
#             str += phrases[i]
#     else:
#         cut2 = cut1 % 14
#         for i in range(cut2,len(phrases)):
#             str += phrases[i]
#         for i in range(cut2):
#             str += '_'
#
#     return str

def solution(phrases, second):
	answer = ''

	display = '______________' + phrases +  '______________'
	# print(display [10:3])
	display = display[second%28:second%28+14]
	answer = display
	return answer


# def solution(phrases, second):
# 	answer = ''
#
# 	display = '______________' + phrases
# 	for i in range(second):
# 		display = display[1:] + display[0]
#
# 	answer = display[:14]
#
# 	return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
phrases = "abc-birthday"
second = 4

for i in range(30):
    ret = solution(phrases, i)
    print(ret)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")