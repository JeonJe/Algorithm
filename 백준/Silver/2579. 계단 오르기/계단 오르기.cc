#include <iostream>
#include <algorithm>
using namespace std;

/*계단 오르는 데는 다음과 같은 규칙이 있다.

계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나,다음 다음 계단으로 오를 수 있다.
연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
마지막 도착 계단은 반드시 밟아야 한다.
따라서 첫 번째 계단을 밟고 이어 두 번째 계단이나, 세 번째 계단으로 오를 수 있다. 
하지만, 첫 번째 계단을 밟고 이어 네 번째 계단으로 올라가거나, 첫 번째, 두 번째, 세 번째 계단을 연속해서 모두 밟을 수는 없다.

각 계단에 쓰여 있는 점수가 주어질 때 이 게임에서 얻을 수 있는 총 점수의 최댓값을 구하는 프로그램을 작성하시오.*/

int main()
{
	int T = 0;
	int arr[301] = { 0, };
	int DP[301][3];
	cin >> T;


	for (int i = 1; i < T + 1; i++) {
		cin >> arr[i];
	}

	DP[1][1] = arr[1]; // 한 계단씩 올라 첫 번째 계단 밟을 경우 
	DP[2][1] = arr[2]; // 두 계단씩 올라 두 번째 계단 밟은 경우 
	DP[2][2] = arr[1] + arr[2]; // 한 계단씩 올라 첫 번째 계단과 두 번째 계단 밟은 경우 

	for (int i = 3; i <= T; i++) {
		DP[i][1] = max(DP[i - 2][1], DP[i - 2][2]) + arr[i]; // 현재 위치에서 2 계단 아래 있는 계단의 큰 값  + 현재 계단 값
		DP[i][2] = max(DP[i - 3][1], DP[i - 3][2]) + arr[i - 1] + arr[i];// 현재 위치에서 3 계단 아래 있는 계단의 큰 값  + 현재보다 한 계단 아래 값 + 현재 계단 값
																		//세번 연속 한 계단 씩 오르지 못하기 때문에 -3
	}

	cout << max(DP[T][1], DP[T][2]) << endl; // 둘 중 큰 값

	return 0;
}