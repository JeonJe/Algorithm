#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(int n) {
	int answer = 0;
	int sum = 0, temp = 0;

	for (int i = 1; i < (n / 2) + 1; ++i) { // 절반을 넘은 숫자를 더하면 어차피 n 의 숫자를 넘음
		sum = 0;    // 합 초기화
		temp = i;   // 초기 시작  숫자
		while (sum < n) 
			sum += temp++; //연속된 수의 합계
		
		if (sum == n) //연속된 수의 합이 n과 같다면 
			answer++; // 답 증가
		
	}
	return answer + 1;

}

int main() {

	cout << solution(15);
}