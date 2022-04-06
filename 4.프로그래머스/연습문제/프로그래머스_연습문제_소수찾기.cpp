#include <string>
#include <vector>

using namespace std;

int solution(int n) {
	int answer = 0;
	vector<bool> arr(n + 1);

	for (int i = 2; i <= n; ++i) {
		if (arr[i] == false) answer++; // 배수라고 체크가 안 되어있다면, 소수

		for (int j = i; j <= n; j += i)    // i가 2일 땐 2,4,6,8 ... 2의 배수 인덱스을 모두 true로
			arr[j] = true;
	}

	return answer;
}