//https://www.acmicpc.net/problem/11047
#include <iostream>

//총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
//동전을 적절히 사용해서 그 가치의 합을 K

using namespace std;

int N;
int K;
int M = 0;
int arr[1000001] = { 0, };

int main() {
	cin >> N >> K;
	for (int i = 1; i < N+1; i++) {
		cin >> arr[i];
	}

	for (int i = N; i > 0; i--) {   // ex) 4200 원에서 
		M += K / arr[i];		    // arr[i] 가 4200 보다 크면 0이 더해짐.
									//arr[i] 가 K 보다 작으면 4200 / 1000 => 4 (횟수) 가 M에 더해짐
		K = K % arr[i];				// 4200 % 1000 이면 나머지 200 원이 K에 갱신 
								   //만약 4200 % 5000 이였으면 나머지인 4200 그대로
	}
	cout << M;
}