#include <stdio.h>
#include <iostream>
using namespace std;

int main() {
	int N; 
	int sum = 0;
	int num = 0;
	scanf("%d", &N);

	getchar(); // 버퍼 비우기
	for (int i = 0; i < N; i++) {
		char ch;
		scanf("%1c", &ch);
		sum += ch - '0';
	}

	cout << sum;

	return 0;
}