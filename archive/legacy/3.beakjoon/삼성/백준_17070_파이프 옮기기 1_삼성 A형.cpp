#include <iostream>
#include <cstring>
#include <queue>

using namespace std;

int N;
int arr[18][18] = { 0, };
int DP[3][18][18] = { 0, };
int r, c = 0;


//DP 또는 BFS 둘다 가능


struct pipe { //파이프의 속성  => 방향, 위치
	int direction, x, y;
};

//DP 버전
//D[0][X][Y] : 가로 파이프가(X, Y)에 도착하는 방법의 수
//D[1][X][Y] : 세로 파이프가(X, Y)에 도착하는 방법의 수
//D[2][X][Y] : 대각선 파이프가(X, Y)에 도착하는 방법의 수
//D[0][1][2] = 1 : 가로 파이프 시작 위치(1, 2)
//출처 : https ://rebas.kr/838 [PROJECT REBAS]


int solve() {
	DP[0][0][1] = 1;    //초기에 파이프 0,0 , 0,1 => 파이프의 머리는 x =1 y = 0 에 위치, 방향은 가로로

	for (int i = 0; i < N; ++i) {
		for(int j = 0; j < N; ++j) {
			if (arr[i][j + 1] == 0) DP[0][i][j + 1] += DP[0][i][j] + DP[2][i][j];   //가로 방향으로 갈 수 있는 경우 => 가로 방향-> 가로방향 또는 대각선방향 -> 가로방향
			if (arr[i + 1][j] == 0) DP[1][i+1][j] += DP[1][i][j] + DP[2][i][j];   //세로 방향으로 갈 수 있는 경우 => 세로 방향-> 세로방향 또는 대각선방향 -> 세로방향
			if (arr[i + 1][j + 1] == 0 && arr[i + 1][j] == 0 && arr[i][j + 1] == 0) 
				DP[2][i + 1][j + 1] += DP[0][i][j] + DP[1][i][j] + DP[2][i][j]; // 세 방향으로 i, j 에 도착 하는 경우의 수 + 대각선으로 i+1 , j+1 으로 가는 수 
		}
	}

	return DP[0][N-1][N-1]+ DP[1][N - 1][N - 1]+ DP[2][N - 1][N - 1];
}

int Dx[] = { 0,1,1 }; // 0: 세로, 1: 대각선 , 2: 가로
int Dy[] = { 1,1,0 };

int solve_bfs() {
	int cnt = 0; // n-1, n-1 지점의 도달 경우의 수 

	queue<pipe> q;
	q.push({ 2, 1, 0 });   //초기에 파이프 0,0 , 0,1 => 파이프의 머리는 x =1 y = 0 에 위치, 방향은 가로로

	while (!q.empty()) {
		pipe curr = q.front(); //파이프 머리 부분 좌표와 방향
		q.pop();

		if (curr.x == N - 1 && curr.y == N - 1)
			cnt++; //종료 조건

		int start = 0;
		int end = 0;
		if (curr.direction == 0) {  // 세로 일 경우 세로, 대각선 이동 경우 확인
			start = 0;
			end = 2;
		}
		else if (curr.direction == 1) // 대각선 일 경우 세로, 대각선,가로  이동 경우 확인
		{
			start = 0;
			end = 3;
		}
		else if (curr.direction == 2) {// 가로 일 경우 가로, 대각선 이동 경우 확인
			start = 1;
			end = 3;
		}

		for (int i = start; i < end; ++i) {
			int ny = curr.y + Dy[i];
			int nx = curr.x + Dx[i];
			int ndirection = i;

			if (nx < N && ny < N && arr[ny][nx] == 0) {
				if (ndirection == 0 || ndirection == 2) // 세로  또는 가로 이동이면 
					q.push({ ndirection, nx, ny });
				else if (ndirection == 1 && !arr[ny][nx - 1] && !arr[ny - 1][nx]) {
					// 대각선이면서 이동하려는 위치의 위, 옆으로 벽이 없어야 함
					q.push({ ndirection,nx,ny });
				}
			}
		}
	}

	return cnt;

}


int main()
{
	cin >> N;
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; ++j) { // 1,1 이 아니라 0,0 에서 시작 N-1까지
			cin >> arr[i][j];
		}
	}

	cout << solve();

	return 0;
}