#include <iostream>
#include <string.h>
#include <algorithm>
using namespace std;

//정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
//
//X가 3으로 나누어 떨어지면, 3으로 나눈다.
//X가 2로 나누어 떨어지면, 2로 나눈다.
//1을 뺀다.
//정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다.연산을 사용하는 횟수의 최솟값을 출력하시오.

int N;
int DP[1000001];
int cnt = 0;

int main()
{
	memset(DP, 0, sizeof(int) * 1000001);
	cin >> N;

	DP[1] = 0;

	for (int i = 2; i <= N; i++) {
		DP[i] = DP[i - 1] + 1; //1을 뺴는 경우 
		if (i % 2 == 0) DP[i] = min(DP[i], DP[i / 2] + 1); // 2으로 나누어지는 경우 
		if (i % 3 == 0) DP[i] = min(DP[i], DP[i / 3] + 1); // 3으로 나누어지는 경우  
	}

	cout << DP[N] << endl;;
	return 0;
}