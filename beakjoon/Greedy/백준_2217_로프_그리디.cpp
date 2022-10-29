#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int N;
vector<int> rope;
vector<int> sum;
int main() {
	cin >> N;
	int num = 0;

	for (int i = 0; i < N; i++) {
		cin >> num;
		rope.push_back(num);
	}

	sort(rope.begin(), rope.end(), greater<int>());  // 로프가 버틸 수 있는 물체의 최대 중량을 내림 차순으로 정렬

	for (int i = 0; i < rope.size(); i++) {  //  병렬 연결된 로프 중 최대 중량을 버틸 수 있는 로프를 사용 할 경우 그 로프만 사용 가능하므로 *1
		sum.push_back(rope[i] * (i + 1));   // 두 번째로 중량을 많이 버티는 로프를 사용하면 최대중량과 2번째 중량 로프가 가능하므로 *2
	}

	num  = *max_element(sum.begin(), sum.end()); // 각 로프들이 병렬로 버틸 수 있는 무대 중 최대의 무게를 가져옴 
	cout << num;

	return 0;
}