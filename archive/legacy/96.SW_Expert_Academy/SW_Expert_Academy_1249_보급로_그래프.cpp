#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstring>
#include <stdlib.h>
#include <queue>

using namespace std;

struct path
{
	int x, y, time;
};

const int MAX = 101;

int shortest_path = 987654321;

int Dy[] = { -1,1,0,0 };
int Dx[] = { 0,0,-1,1 };

int map[MAX][MAX] = { 0, };
int dist[MAX][MAX] = { 0, };


int T = 0;
int N = 0;


int BFS() {
	queue<path> q;
	q.push({ 0,0,1 }); //시작 위치 , time을 0으로 하면 안됨

	while (!q.empty()) {

		int x = q.front().x;  // 현재 확인 위치 
		int y = q.front().y;
		int time = q.front().time;
		q.pop();

		//도착지로 도착한 여러가지 경로 중 최소값을 가진 경로찾기
		if (x == N - 1 && y == N - 1) {
			if (shortest_path > time) shortest_path = time;
			continue;
		}

		for (int dir = 0; dir < 4; dir++) {
			int ny = x + Dy[dir];
			int nx = y + Dx[dir];

			//새로운 위치가 맵 밖일 경우 예외처리
			if (ny < 0 || ny >= N || nx < 0 || nx >= N) continue;

			// 현재 위치에서 새로운 위치(ny,nx) 로 가는 경로의 시간이 
			// 가장 짧다고 저장한 경로의 시간보다 작은 경우, 업데이트
			if (dist[ny][nx] == 0 || time + map[ny][nx] < dist[ny][nx]) {
				q.push({ ny, nx, time + map[ny][nx] });
				dist[ny][nx] = time + map[ny][nx];

			}

		}
	}

	return  shortest_path - 1;
}

int main() {
	cin >> T;
	for (int i = 1; i < T + 1; ++i) {
		cin >> N;

		memset(map, 0, sizeof(map)); //map 초기화
		memset(dist, 0, sizeof(dist)); //dist 초기화
		shortest_path = 987654321;

		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				scanf("%1d", &map[i][j]);
			}
		}

		cout << "#" << i << " " << BFS() << endl;

	}
	return 0;
}