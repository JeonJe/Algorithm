# XX 게임에선 캐릭터는 자신과 공격력이 같거나 자신보다 공격력이 작은 몬스터에게 이깁니다 . 내가 가
# 진 캐릭터가 최대 몬스터 몇 마리를 이길 수 있는지 구하려 합니다 . 단 , 한 캐릭터는 한 번만 싸울 수
# 있습니다
# 예를 들어 , 세 몬스터의 공격력이 각각 [1, 4, 이고 , 내가 가진 두 캐릭터의 공격력이 각각 [1, 이라
# 면 첫 번째 캐릭터는 첫 번째 몬스터와 , 두 번째 캐릭터는 세 번째 몬스터와 싸워서 이길 수 있습니
# 다 . 따라서 이길 수 있는 몬스터 수는 최대 2 마리입니다 .
# 모든 몬스터의 공격력을 담은 리스트 enemies, 내가 가진 모든 캐릭터의 공격력을 담은 리스 트
# armies 가 매개변수로 주어질 때 , 내 캐릭터로는 최대 몬스터 몇 마리를 이길 수 있는지 return 하도
# 록 solution 함수를 작성해주세요

def solution(enemies, armies):
    #여기에 코드를 작성해주세요.
    answer = 0
    enemies.sort()
    armies.sort()

    for a in armies:
        temp = -1
        for e in range(len(enemies)):
            if a>= enemies[e]:
                answer+=1
                temp = e
                break

        if temp != -1:  # 현재 아군이 적을 이겼으면
            enemies.pop(e) # 이긴 적 삭제

    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
armies1 = [1,3]
enemies1 = [1,4,3]

ret1 = solution(enemies1, armies1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

enemies2 = [1, 1, 1]
armies2 = [1, 2, 3, 4]
ret2 = solution(enemies2, armies2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")