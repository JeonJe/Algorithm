#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <queue>
#include <cstring>
#include <stdio.h>

using namespace std;
int N, M;

int map[1001][1001];
int cache[1001][1001][2];  //여기서 벽이 뚫린 여부, 최단 경로가 몇 번인지도 확인가능
						  

int Dx[] = { 0,0,-1,1 };
int Dy[] = { -1,1,0,0 };
int solve() {

	queue<pair<int, pair<int, int>>> q; // 벽 뚫은 횟수,  y, x
	q.push({  1, { 0,0 } }); // 1번 뚫을 기회가 있는 0,0 부터 시작
	cache[0][0][1] = 1; 

	while (!q.empty()) {
		int bw = q.front().first;
		int y = q.front().second.first;
		int x = q.front().second.second;
	
		q.pop();

		if (0 > y || N <= y || 0>x || M <= x) continue; //범위 밖이면 반복문으로
		if (y == N - 1 && x == M - 1) return cache[y][x][bw];

		for (int i = 0; i < 4; ++i) {
			int new_y = y + Dy[i];
			int new_x = x + Dx[i];

			if (0 <= new_y && new_y < N && 0 <= new_x && new_x < M) {  //판의 범위 안 
				if (map[new_y][new_x] == 0 && cache[new_y][new_x][bw] == 0 ) { // 방문한적없으면 
					cache[new_y][new_x][bw] = cache[y][x][bw] + 1; // y,x 로 가는 경우의 수 + 1
					q.push({ bw, { new_y, new_x } });
				}
				if (map[new_y][new_x] == 1 &&  bw == 1) { // 새로 갈려는 곳이 막혀있고, 뚫을 기회가 있다면 
					cache[new_y][new_x][bw-1] = cache[y][x][bw] + 1; // y,x 로 가는 경우의수 + 1, 하지만 bw 은 감소
					q.push({ bw-1 , { new_y, new_x } });
				}
			}

		}

	}

	return -1;

}
int main()
{
	cin >> N >> M; // N 이 row 의 수 (세로) , M은 col의 수 (가로)

	memset(map, 0, sizeof(map));
	memset(cache, 0, sizeof(cache));

	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < M; ++j)
			scanf("%1d", &map[i][j]);
	}


	cout << solve();
	return 0;

}