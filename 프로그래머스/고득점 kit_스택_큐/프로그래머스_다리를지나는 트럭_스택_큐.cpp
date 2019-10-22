//https://programmers.co.kr/learn/courses/30/lessons/42583

#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <numeric> //accumulate을 쓰기 위해 사용
using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
	int answer = 0;
	vector<int> bridge;

	for (int i = 0; i < bridge_length; ++i)
		bridge.emplace_back(0); // push 보다 빠른 emplace_back, 다리의 길이만큼 0으로 채움

	while (!bridge.empty()) { //다리의 길이 
		answer++;	//시간 증가 
		bridge.erase(bridge.begin()); //길이 하나 삭제 ( 트럭 하나가 사용하기 때문에 )

		if (truck_weights.size() > 0) { // 대기 트럭이 존재하면
			int sum = accumulate(bridge.begin(), bridge.end(), 0); // 다리를 건너는 트럭의 무게 합
			if (sum + truck_weights[0] <= weight) { // 건너는 트럭과 대기트럭의 무게를 합한 무게를 견딜 수 있으면
				bridge.emplace_back(truck_weights[0]); // 대기 트럭을 다리에 올림
				truck_weights.erase(truck_weights.begin()); //대기 트럭의 목록에서 삭제
			}
			else {
				bridge.emplace_back(0); // 대기트럭이 올라오지 못하면 0을 뒤에 삽입
			}
		} // 다리의 길이만큼 시간이 경과해야하기 때문에 대기 트럭이 존재하지 않아도 
		//계속 반복문을 돌며 다리를 건너는 트럭이 모두 지날때까지 시간증가
	}

	return answer;
}

int main() {

	int length = 2;
	int weight = 10;
	vector<int> truck{ 7,4,5,6 };
	cout << solution(length, weight, truck);
	return 0;
}