#include <iostream>
#include <vector>
using namespace std;

//2부터 N까지의 모든 소수의 합을 구하세요.N이 7이라면{ 2,3,5,7 } = 17을 출력 하시면 됩니다.
//N의 범위는 2이상 10, 000, 000이하 입니다.효율성 테스트의 모든 시간 제한은 1초입니다.
//소수의 합에 좋은 알고리즘은 '아리토스테네스의 체'

//소수 찾기의 경우에는
//N = A * B 가 소수가 아님을 이용
//즉, 어떤 정수 n의 제곱근까지의 수 중 한 개의 수에 대해서라도 나누어떨어지면 소수가 아니다.
//
//int rootNumber = sqrt(number); 
//for (int n = 3; n <= rootNumber; n += 2) 
//	if (number % n == 0)  return false;
//

int main() {

	int n = 0;
	cin >> n;
	long long answer = 0;
	vector<bool> arr(n + 1);

	for (int i = 2; i <= n; ++i) {
		if (arr[i] == false) answer += i; // 배수라고 체크가 안 되어있다면, 합산에 현재 수를 더함


		for (int j = i; j <= n; j += i)    // i가 2일 땐 2,4,6,8 ... 2의 배수 인덱스을 모두 true로
			arr[j] = true;
		
	}
	cout << answer;
	return 0;
}

