#include <iostream>
#include <cstring>
using namespace std;

// N = 1: 1              1개
// N = 2: 00 11          2개 
// N = 3: 001 100 111    3개   => N = 1 +  N = 2 
// N = 4: 0000 0011 1100 1001 1111  5개 => N = 2 + N = 3 
// N = 5: 00001 10000 11111 11100 00111 00100 10011 11001 이므로 8개 => N = 3 일 때  3  +  N = 4 일 때 5
// 결국은 피보나치 수열
int main() {
	int N;

	cin >> N;

	int tile[1000001];
	memset(tile, 0, sizeof(tile));
	tile[0] = 1;
	tile[1] = 2;

	for (int i = 2; i <= N; i++)	//피보나치 
		tile[i] = (tile[i - 1] + tile[i - 2]) % 15746; //N이 1,000,000 까지 이면 int 형으로 표현을 못함 
													 // => 문제에서 15746의 나머지 요구했으므로 나머지를 대입

	cout << tile[N - 1] << endl;

	return 0;
}