#include <iostream>
#include <string.h>

using namespace std;

int T = 0;
int M, N, K;
int cnt;
bool visit[50][50];

int x_point[4] = { 1,-1, 0, 0 };
int y_point[4] = { 0, 0 , -1, 1 };


void dfs(int** arr, int y, int x) {
	visit[y][x] = true; // 방문 표시 

	for (int z = 0; z < 4; z++) {
		int new_x = x + x_point[z];
		int new_y = y + y_point[z];  // 네 방향 확인

		if ( 0 <= new_x && new_x < M && 0 <= new_y && new_y < N ) {
			if (visit[new_y][new_x] == false && arr[new_y][new_x]) dfs(arr, new_y, new_x); // 방문하지 않았고 배추가있으면 건너감
		}
	}
}

int main()
{

	cin >> T;
	for (int i = 1; i < T + 1; i++) {
		cin >> M >> N >> K; // M이 가로 

		int** arr = new int* [N];
		for (int i = 0; i < N; i++) {
			arr[i] = new int[M];
			memset(arr[i], 0, sizeof(int) * M);
		}
		for(int i = 0; i < 50; i++)
		memset(visit[i], false, sizeof(bool) * 50);	//초기화

		int X, Y;
		for (int i = 0; i < K; i++) {
			cin >> X >> Y;
			arr[Y][X] = 1;	//배추 심기

		}

		cnt = 0;

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (arr[i][j] && visit[i][j] == false) {
					dfs(arr, i, j);
					cnt++;	//벌레수 체크 
	
				}
			}

		}

		cout << cnt << endl;

	}

	return 0;
}