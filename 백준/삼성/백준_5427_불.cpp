#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <stdio.h>
#include <string>
#include <cstring>
#include <queue>

using namespace std;

int T;
int h, w;

const int MAX = 1000;
int Dx[] = { 0,0,-1,1 };
int Dy[] = { -1,1,0,0 };
char map[MAX][MAX];
bool visit[MAX][MAX];


//매초마다 불은 동서남북 방향으로 퍼져나감
//벽에는 불이 붙지 않음
//상근이는 매초마다 동서남북 인접 칸으로 이동가능
//벽을 통과할 수 없고, 불이 옮겨진 칸 또는 이제 불이 붙으려는 칸으로 이동x
//상근이가 있는 칸에 불이 옮겨옮과 동시에 다른 칸 이동 가능
// 빌등을 탈출하는데 가장 빠른 시간 출력, 빌딩을 탈출할 수 없으면 불가능	

// . : 빈공간
// # : 벽
// @ : 상근이 위치
// '*' : 불
int solve() {
	int time = 0;

	memset(visit, false, sizeof(visit));
	queue<pair<int, int>> q;
	queue<pair<int, int>> fq;


	for (int i = 0; i < h; ++i) {
		for (int j = 0; j < w; ++j) {
			if (map[i][j] == '@') {
				visit[i][j] = true; //상근이 위치
				q.push({ i, j }); // y, x
		
			}
			else if (map[i][j] == '*') { // 불 위치 입력 
				fq.push({ i, j }); // y, x
			}
		}
	}

	bool exit = false;
	while (!q.empty()) {
		time++; // 시간 증가

		int current_move = q.size();
		for (int m = 0; m < current_move; ++m) { // 1초에 상근이가 이동할 수 있는 경우 확인
			int y = q.front().first;
			int x = q.front().second; // 이번 위치의 x, y 좌표

			q.pop();

			if (map[y][x] == '*') continue;  // 이번 상근이 위치가 불이 있는 곳이면 다음거 확인.

			for (int i = 0; i < 4; ++i) { // 아직 탈출 못했으면 4방향에 대해 이동 확인
				int ny = y + Dy[i];
				int nx = x + Dx[i];

				if (nx < 0 || nx >= w || ny < 0 || ny >= h) {  // 다음 위치가 map 밖이면 상근이 탈출
					exit = true;
					break;
				}

				if (map[ny][nx] == '.' && visit[ny][nx] == false) { // 다음 위치가 빈 공간이고 방문한 적 없으면
					visit[ny][nx] = true; // 방문 표시 
					q.push({ ny,nx });  // 상근이 방문 큐에 추가 
				}
			}

		}
		if (exit) return time; // 상근이가 빌딩을 탈출했으면 반복문 break 아니라면 불 이동

			int current_fmove = fq.size(); // 이번 시간에 불이 욺직일 수 있는 경우들

			for (int m = 0; m < current_fmove; ++m) {
				int y = fq.front().first;
				int x = fq.front().second; // 이번 불 위치의 x,y 좌표
				fq.pop();

				for (int i = 0; i < 4; ++i) { // 불 4방향 이동 확인
					int ny = y + Dy[i];
					int nx = x + Dx[i];

					if (nx < 0 || nx >= w || ny < 0 || ny >= h) continue; // 판 밖으로 나가면 확인 x

					if (map[ny][nx] == '.') { // 다음 이동 장소가 빈 공간이라면 
						map[ny][nx] = '*'; // 불로 변경 
						fq.push({ ny,nx });  // 불 방문 큐에 추가 
					}
				}
			}
	}

	return -1;
}
int main()
{
	cin >> T;
	for (int t = 0; t < T; t++) {
		cin >> w >> h;
		memset(map, 0, sizeof(map));
		for (int i = 0; i < h; ++i) {
			getchar(); // 입력 버퍼 비우기
			for (int j = 0; j < w; ++j) {
				map[i][j] = getchar(); //한 글자씩 받기 
			}
		}

		int result = solve();
		if (result == -1) cout << "IMPOSSIBLE" << endl;
		else cout << result << endl;

	}

	return 0;
}