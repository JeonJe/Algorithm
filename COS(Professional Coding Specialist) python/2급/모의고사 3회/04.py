# 단어 시험을 치르고 있습니다. 각 답안에 적힌 단어의 알파벳 중 틀린 개수를 세려고 합니다. 예를
# 들어 학생들이 “python”이라는 단어에 대한 답안을 [“pythan”, “pithon”, “python”, “pithun”,
# “pythom”, “python”]으로 제출했다면, “pythan” : 1번, ,“pithon” : 1번, “python” : 0번, “pithun” : 2
# 번, “pythom” :2번 , “python” :0 번 틀렸습니다.
# 시험을 치른 모든 학생의 답안을 담은 리스트 answers와 정답인 단어 correct가 매개변수로 주어
# 질 때 틀린 총 횟수를 return하도록 solution함수를 완성해 주세요.

def solution(answers, correct):
    #여기에 코드를 작성해주세요
    answer = 0
    for x in answers:
        for i in range(len(x)):
            if x[i] != correct[i]:
                answer+=1

    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
answers = ["pythan", "pithon", "python",
           "pithun", "pythom", "python"]
correct = "python"
ret = solution(answers, correct)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
