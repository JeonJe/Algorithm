//https://programmers.co.kr/learn/courses/30/lessons/43165

#include <string>
#include <vector>
#include <queue>

using namespace std;

int cnt;

void dfs(vector<int> numbers, int target, int sum, int depth) {
	if (depth >= numbers.size()) { // 숫자를 한 개씩 더하다가 배열의 크기만큼 커지면
		if (sum == target) // 배열의 합이 타겟과 같다면 cnt 증가
			cnt++;
		return;              // dfs 리턴
	}
	dfs(numbers, target, sum + numbers[depth], depth + 1); // 다음 숫자를 더함
	dfs(numbers, target, sum - numbers[depth], depth + 1); // 다음 숫자를 뺌
}

int solution(vector<int> numbers, int target) {
	
	dfs(numbers, target, numbers[0], 1); // 첫번 째 숫자를 더할 경우
	dfs(numbers, target, numbers[0] * -1, 1); //두번 째  숫자를 뺄 경우

	return cnt;
}

