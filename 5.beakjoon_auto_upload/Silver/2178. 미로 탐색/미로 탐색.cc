#include <iostream>
#include <cstring>
#include <queue>
using namespace std;

const int MAX = 101;
int N, M;

int arr[MAX][MAX];
bool visit[MAX][MAX];
int maze[MAX][MAX];

queue <pair<int, int>> q;

int x_point[4] = { -1, 1, 0, 0 };
int y_point[4] = { 0,  0, -1, 1 };


void bfs() {

	q.push(make_pair(0, 0));	// 첫 지점을 queue 에 삽입
	maze[0][0] = 1;				
	visit[0][0] = true;			//방문 표시

	int new_y, new_x;
	pair<int, int> current;
	
	while (!q.empty()) {
		 current = q.front();	
		 q.pop();

		for (int i = 0; i < 4; i++) {
			 new_y = current.first + y_point[i]; // 주변에 탐색 
			 new_x = current.second + x_point[i];

			if (0 <= new_x && new_x < M && 0 <= new_y && new_y < N ) {
				if (visit[new_y][new_x] || arr[new_y][new_x] == 0) continue;

				visit[new_y][new_x] = true;		//주변에 방문하지 않은 1이있으면
				q.push(make_pair(new_y, new_x));		//큐에 삽입
				maze[new_y][new_x] = maze[current.first][current.second] + 1;
			}
		}
	}
	return;
}

int main()
{
	cin >> N >> M; //N이 세로 , M이 가로

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			scanf("%1d", &arr[i][j]);
		}
	}

	for (int i = 0; i < MAX; i++)
		memset(visit[i], false, sizeof(bool) * MAX);

	bfs();

	cout << maze[N - 1][M - 1] << endl;
}