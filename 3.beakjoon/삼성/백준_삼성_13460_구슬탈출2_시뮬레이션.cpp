#include <iostream>
#include <stdio.h>
#include <queue>

struct INFO {
	int ry, rx, by, bx, count;  //count 는 몇번 움직였는지 
};

using namespace std;
const int MAX = 10;

char map[MAX][MAX + 1];
INFO start;
int visit[MAX][MAX][MAX][MAX] = { 0, };

int Dy[] = { -1,1,0,0 };
int Dx[] = { 0,0, -1,1 };

int bfs() {
	int ret = -1;
	queue<INFO> q;
	q.push(start);
	visit[start.ry][start.rx][start.by][start.bx] = 1; // 방문 표시 


	while (!q.empty()) {
		INFO cur = q.front(); q.pop();

		if (cur.count > 10) break;
		if (map[cur.ry][cur.rx] == 'O' && map[cur.by][cur.bx] != 'O') {
			ret = cur.count;
			break;
		}

		for (int i = 0; i < 4; ++i) {
			int next_ry = cur.ry;
			int next_rx = cur.rx;
			int next_by = cur.by;
			int next_bx = cur.bx;

			while (1) {  // 빨간공 이동
				if (map[next_ry][next_rx] != '#' && map[next_ry][next_rx] != 'O') {
					next_ry += Dy[i]; next_rx += Dx[i];  // 기울임으로 계속 방향 갱신
				}
				else {
					if (map[next_ry][next_rx] == '#') {  // 다음으로 이동했는데 벽이였다면 
						next_ry -= Dy[i]; next_rx -= Dx[i]; // 벽 이전으로 이동 
					}
					break;
				}
			}
			while (1) {  //파란공 이동
				if (map[next_by][next_bx] != '#' && map[next_by][next_bx] != 'O') {
					next_by += Dy[i]; next_bx += Dx[i];  // 기울임으로 계속 방향 갱신
				}
				else {
					if (map[next_by][next_bx] == '#') {  // 다음으로 이동했는데 벽이였다면 
						next_by -= Dy[i]; next_bx -= Dx[i]; // 벽 이전으로 이동 
					}
					break;
				}
			}
			if (next_ry == next_by && next_rx == next_bx) { //한칸에 빨간공, 파란공이 모두 있는 경우 
				if (map[next_ry][next_rx] != 'O') {  //구멍인 경우에는 나왔기 때문에 처리 안해도 됨
					int red_dist = abs(next_ry - cur.ry) + abs(next_rx - cur.rx);
					//기울임으로 움직인 빨간 구슬거리, 가로 세로중 어느방향으로 움직인지는 모르나 둘 중 하나는 0
					int blue_dist = abs(next_by - cur.by) + abs(next_bx - cur.bx); //기울임으로 파란 구슬 움직인 거리
					if (red_dist > blue_dist) {
						next_ry -= Dy[i]; next_rx -= Dx[i]; // 한칸 이전으로 이동 
					}
					else {
						next_by -= Dy[i]; next_bx -= Dx[i]; // 한칸 이전으로 이동 
					}
				}
			}
			if (visit[next_ry][next_rx][next_by][next_bx] == 0) { // 기울임 후 방문한적이 없는 곳이라면?
				visit[next_ry][next_rx][next_by][next_bx] = 1; // 방문으로 표시 
				INFO next;
				next.ry = next_ry;
				next.rx = next_rx;
				next.by = next_by;
				next.bx = next_bx;
				next.count = cur.count + 1;  //새로운 위치를 담고 queue에 다시 넣기 
				q.push(next);
			}
		}
	}
	return ret;
}
int main() {
	int N, M; // N은 세로 (y), M은 가로(x)
	cin >> N >> M;

	for (int i = 0; i < N; ++i) {
		getchar(); //버퍼 비우기
		for (int j = 0; j < M; ++j) {
			map[i][j] = getchar();
			if (map[i][j] == 'R') {
				start.ry = i, start.rx = j;
			}
			if (map[i][j] == 'B') {
				start.by = i, start.bx = j;
			}
		}
	}
	start.count = 0;
	cout << bfs() << endl;


	return 0;
}