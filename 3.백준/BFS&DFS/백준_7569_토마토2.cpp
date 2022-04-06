#include <iostream>
#include <cstring>
#include <queue>

using namespace std;

const int MAX = 101;
int N, M, H; // M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다.

int arr[MAX][MAX][MAX];
bool visit[MAX][MAX][MAX];
int box[MAX][MAX][MAX];

queue <pair<int,pair<int, int>>> q;

int Dx[] = { -1, 1, 0, 0,0,0 };
int Dy[] = { 0,  0, -1, 1 ,0,0 };
int Dz[] = { 0,0,0,0,-1,1 };   

void bfs() {

	for (int k = 0; k < H; k++)
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {		// 처음에 익은 토마토들 위치 파악
				if (arr[k][i][j] == 1) {
					q.push(make_pair(k,make_pair(i, j)));	//큐에 삽입
					visit[k][i][j] = true;			//방문 표시
					box[k][i][j] = 0;				// 0일차 
				}
			}
		}

	int new_y, new_x, new_z;
	pair<int,pair<int, int> >current;

	while (!q.empty()) {
		current = q.front();
		q.pop();

		for (int i = 0; i < 6; i++) {
			new_y = current.second.first + Dy[i]; // 주변에 탐색 
			new_x = current.second.second + Dx[i];
			new_z = current.first + Dz[i];

			if (0 <= new_x && new_x < M && 0 <= new_y && new_y < N &&0 <= new_z && new_z < H) {
				if (visit[new_z][new_y][new_x] || arr[new_z][new_y][new_x] == -1 || arr[new_z][new_y][new_x] == 1) continue;
				// 토마토가 없거나 익었으면 다음으로

				visit[new_z][new_y][new_x] = true;		//주변에 익지 않은 토마토가 있으면 방문
				arr[new_z][new_y][new_x] = 1;			//토마토 익음
				q.push(make_pair(new_z, make_pair(new_y, new_x)));		//큐에 삽입
				box[new_z][new_y][new_x] = box[current.first][current.second.first][current.second.second] + 1; // 현재까지 걸린 일  + 1
			}
		}
	}
	return;
}

int main()
{
	cin >> M >> N >> H; //N이 세로 , M이 가로 , H는 세로 


	memset(visit, false, sizeof(bool) * MAX);
	memset(box, 0, sizeof(int));

	for (int k = 0; k < H; k++)
		for (int i = 0; i < N; i++)
			for (int j = 0; j < M; j++)
				cin >> arr[k][i][j];
		
	bfs();

	int max = -1;
	for (int k = 0; k < H; k++)
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (arr[k][i][j] == 0) {	// 익지 못한 토마토가 있을 경우 
					cout << "-1" << endl;
					return 0;
				}
				else if (max < box[k][i][j]) max = box[k][i][j]; // 모두 익을 때 까지 걸린 일 수 
			}
		}
	cout << max << endl;

	return 0;

}
