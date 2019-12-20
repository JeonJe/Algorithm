# 아래와 같이 벽이 여러 개 있을 때 , 벽 2 개를 제외한 나머지 벽을 제거하여 물을 최대한 담으려 합니
# 다 . 물은 두 벽 사이의 거리 x 두 벽 중 낮은 벽의 높이 리터 만큼 담을 수 있으며 , 두 벽의 거리는
# 두 벽의 위치 차이입니다
# 모든 벽의 위치와 높이를 담은 2 차원 리스트 walls 가 매개변수로 주어질 때 , 물을 최대 몇 리터나 담
# 을 수 있는지 return 하도록 solution 함수를 작성했습니다 . 그러나 , 일부 코드가 잘못되어 코드가 바
# 르게 동작하지 않습니다 . 주어진 코드가 모든 입력을 바르게 처리하도록 코드를 수정해주세요 . 코드는
# 한 줄 만 수정해야 합니다
def solution(walls):
    answer = 0
    for i in range(len(walls)):
    	for j in range(i+1, len(walls)):
    		area = 0
    		if walls[i][1] < walls[j][1]:  # 높이
    			area = walls[i][1] * (walls[j][0] - walls[i][0])
    		else:
    			area = walls[j][1] * (walls[j][0] - walls[i][0])
    		if answer < area:
    			answer = area
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
walls = [[1, 4], [2, 6], [3, 5], [5, 3], [6, 2]]
ret = solution(walls)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")