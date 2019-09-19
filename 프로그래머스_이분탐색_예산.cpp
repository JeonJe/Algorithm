#include <string>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int solution(vector<int> budgets, int M) {

	sort(budgets.begin(), budgets.end()); //함수정렬 

	int low = 0;
	int high = *max_element(budgets.begin(), budgets.end()); // 예산 중 가장 큰 값

	long sum = 0;
	int answer = 0;
	int mid = 0;

	while (low <= high) {
		mid = (low + high) / 2;
		sum = 0;

		for (int i : budgets) {
			if (mid > i) sum += i;  // 요청한 예산이 범위의 중간 값보다 작을 때 
			else sum += mid;    // 요청한 예산이 범위의 중간 값보다 클 때, mid 를 더함 
		}
		if (sum > M) {              //에산의 총합이 입력한 예산 보다 크면
			high = mid - 1;     // high 줄이기
		}
		else {
			answer = mid;       //예산의 총합이 입력한 예산 보다 작으면 가능한 한 최대의 총 예산으로 나눠줄수있음
								// 현재 mid 를 answer로 넣기
			low = mid + 1;        // low 늘리기
		}

	}
	return answer;
}