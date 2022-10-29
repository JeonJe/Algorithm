#include <iostream>
#include <cstring>
#include <queue>

using namespace std;

const int MAX = 1001;
int N, M;

int arr[MAX][MAX];
bool visit[MAX][MAX];
int box[MAX][MAX];

queue <pair<int, int>> q;

int x_point[4] = { -1, 1, 0, 0 };
int y_point[4] = { 0,  0, -1, 1 };


void bfs() {

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {		// 처음에 익은 토마토들 위치 파악
			if (arr[i][j] == 1) {
				q.push(make_pair(i, j));	//큐에 삽입
				visit[i][j] = true;			//방문 표시
				box[i][j] = 0;				// 0일차 
			}
		}
	}

	int new_y, new_x;
	pair<int, int> current;

	while (!q.empty()) {
		current = q.front();		
		q.pop();

		for (int i = 0; i < 4; i++) {
			new_y = current.first + y_point[i]; // 주변에 탐색 
			new_x = current.second + x_point[i];

			if (0 <= new_x && new_x < M && 0 <= new_y && new_y < N) {
				if (visit[new_y][new_x] || arr[new_y][new_x] == -1 || arr[new_y][new_x]== 1) continue; 
				// 토마토가 없거나 익었으면 다음으로

				visit[new_y][new_x] = true;		//주변에 익지 않은 토마토가 있으면 방문
				arr[new_y][new_x] = 1;			//토마토 익음
				q.push(make_pair(new_y, new_x));		//큐에 삽입
				box[new_y][new_x] = box[current.first][current.second] + 1; // 현재까지 걸린 일  + 1
			}
		}
	}
	return;
}

int main()
{
	cin >> M >> N; //N이 세로 , M이 가로
			
	for (int i = 0; i < MAX; i++) {
		memset(visit[i], false, sizeof(bool) * MAX);
		memset(box[i], 0, sizeof(int) * MAX);
	}

	for (int i = 0; i < N; i++)
		for (int j = 0; j < M; j++)
			cin >> arr[i][j];
	
	bfs();

	int max = -1;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (arr[i][j] == 0) {	// 익지 못한 토마토가 있을 경우 
				cout << "-1" << endl;
				return 0;
			}
			else if (max < box[i][j]) max = box[i][j]; // 모두 익을 때 까지 걸린 일 수 
		}
	}
	cout << max << endl;

	return 0;

}