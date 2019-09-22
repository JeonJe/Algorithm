#include <string>
#include <vector>

using namespace std;
int answer = -1;

void dfs(int N, int min, int num, int number) {
	if (min > 8) return; // 최솟값이 8보다 크면 -1을 return 
	if (num == number) {  // 종료 조건, num 이라는 변수에 숫자를 조합해가며 입력한 값이 number와 같아질때
		if (min < answer || answer == -1) {  // 만약 최솟값이 이전에 계산된 answer 보다 작거나 answer 가 -1 일 경우
			answer = min; // min을 최솟값으로 저장
		}
		return;
	}

	int NN = 0;
	for (int i = 0; i < 8; i++) {	// 8번 내 계산하기 
		NN = NN * 10 + N; // N, NN, NNN, NNNN ... NNNNNNNN

		// 첫번 째 dfs 콜  for 반복문 수행 : 0 +-*/ 5 -> ..... -> 0 +-*/ 55555555 

		// 두번 째 dfs 콜  for 반복문 수행 : (0 + 5): 5 +-*/ 5 -> ..... -> 5 +-*/ 55555555 
		// - * / 연산은 안됨    

		// 세번 째 dfs 콜  for 반복문 수행 : (5 + 5): 10 +-*/ 5 -> ..... -> 10 +-*/ 55555555
		// 세번 째 dfs 콜  for 반복문 수행 : (5 / 5): 1 +-*/ 5 -> ..... -> 1 +-*/ 55555555
		// 세번 째 dfs 콜  for 반복문 수행 : (5 * 5): 25 +-*/ 5 -> ..... -> 25 +-*/ 55555555
		//  - 일 경우에는 0 이므로 첫번째 dfs 콜에서 수행
		// .... 

		dfs(N, min + 1 + i, num + NN, number); 
		dfs(N, min + 1 + i, num - NN, number);
		dfs(N, min + 1 + i, num * NN, number);
		dfs(N, min + 1 + i, num / NN, number);
	}
}

int solution(int N, int number) {
	dfs(N, 0, 0, number);
	return answer;
}
