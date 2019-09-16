#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
	int answer = 0;
	int num_lost = lost.size();

	for (int i = 0; i < lost.size(); i++) {
		for (int j = 0; j < reserve.size(); j++) {
			if (lost[i] == reserve[j]) { // 체육복을 빌려줄 수 없으나 수업을 들을 수 있음.
				lost.erase(lost.begin() + i);  //체육복을 빌릴 필요가 없음
				reserve.erase(reserve.begin() + j); // 여벌이 없기 때문에 reserv에서 삭제
				i--;
				j--;        //크기가 하나씩 줄음
				num_lost--; // 잃어버린 사람의 수가 1명 줄었음
			}
		}
	}

	for (int i = 0; i < lost.size(); i++) {
		for (int j = 0; j < reserve.size(); j++) {
			if (lost[i] - 1 == reserve[j] || lost[i] + 1 == reserve[j]) { // 주변에 여벌이 있는 학생이 존재
				reserve.erase(reserve.begin() + j);  // 여벌을 빌려 줬기 때문에 reserve에서 삭제
				num_lost--;                           // 잃어버린 사람의 수가 1명 줄었음
				break;
			}
		}
	}
	return n - num_lost;
}