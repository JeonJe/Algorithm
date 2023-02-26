#include <iostream>
#include <string.h>
#include <algorithm>
using namespace std;
/*
위 그림은 크기가 5인 정수 삼각형의 한 모습이다.

맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때,
이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라.
아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.

삼각형의 크기는 1 이상 500 이하이다. 삼각형을 이루고 있는 각 수는 모두 정수이며, 범위는 0 이상 9999 이하이다.
*/
int main() {
	int n;

	cin >> n;
	int **arr = new int*[n + 1];
	int **DP = new int*[n + 1];

	for (int i = 0; i < n + 1; i++) {
		arr[i] = new int[n + 1];
		DP[i] = new int[n + 1];
		memset(arr[i], 0, sizeof(int)*n + 1);
		memset(DP[i], 0, sizeof(int)*n + 1);
	}


	for (int i = 0; i < n; i++) {
		for (int j = 0; j < i + 1; j++) {
			cin >> arr[i][j];
		}
	}

	DP[0][0] = arr[0][0];

	for (int i = 1; i < n; i++) {
		for (int j = 0; j < i + 1; j++) {
			if (j == 0)  //i번 째 줄 가장 왼쪽일 경우 
				DP[i][j] = DP[i - 1][j] + arr[i][j];

			else if (i == j)  //i번 째 줄 중간일 경우 
				DP[i][j] = DP[i - 1][j - 1] + arr[i][j];

			else  //i번 째 줄 가장 오른쪽일 경우 
				DP[i][j] = max(DP[i - 1][j], DP[i - 1][j - 1]) + arr[i][j];

		}

	}

	int MAX = DP[n - 1][0]; // 마지막 줄의 가장 왼쪽 값부터 확인

	for (int i = 0; i < n; i++)
		if (DP[n - 1][i] > MAX)
			MAX = DP[n - 1][i];

	cout << MAX << endl;


}