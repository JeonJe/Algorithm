#include <iostream>
#include <queue>

using namespace std;

const int MAX = 20;

struct SHARK {  //상어가 가지고 있는 특성
	int y, x, time; // time 은 물고기를 모두 먹을때까지 걸리는 시간
};


int map[MAX][MAX];
int N;

int Dy[] = { -1,1,0,0 };
int Dx[] = { 0,0,1,-1 };

int shark_size, shark_eat; //상어의 크기와 먹은 물고기 수
SHARK shark; //맵의 있는 상어의 정보 

int solve() {
	int answer=0;

	bool is_map_update = true;

		while (is_map_update) { // 상어가 먹을 수 있는 물고기가 있을 때까지 
			is_map_update = false;

			bool visited[MAX][MAX] = { false, }; //각 라운드 마다 새로 visited 사용
			visited[shark.y][shark.x] = true;    //현재 상어 위치 방문 표시

			queue<SHARK> q; //라운드마다 새로운 큐를 넣고 상어의 위치 삽입
			q.push(shark);

			SHARK favorite; // 상어가 먹을 물고기 정보
			favorite.y = 20; favorite.time = -1; // 지도의 가장 큰 값으로 y초기화
						   						//그 이유는 y값 보다 작은 물고기(위쪽) 을 먼저 먹기 위해 

			while (!q.empty()) {  // 물고기 위치 파악 
				SHARK cur = q.front(); q.pop();

				if (favorite.time != -1 && favorite.time < cur.time)
					break; // 먹을려는 물고기의 시간이 현재보다 작으면 볼 필요 없음
							//가장 가까운 물고기는 잡았다라고 판단
				
				if (map[cur.y][cur.x] < shark_size && map[cur.y][cur.x]!=0) { //상어가 물고기를 먹을 수 있다면
					is_map_update = true; //먹을 물고기가 있다  표시

					//먹을려는 물고기들 중 위쪽에 있고 가장 왼쪽에 있는 놈인지를 확인
					if (favorite.y > cur.y || (favorite.y == cur.y && favorite.x > cur.x)) {
						favorite = cur;
					}

				}

				for (int dir = 0; dir < 4; ++dir) { // 4방향으로 탐색을 돌며 
					SHARK next;
					next.y = cur.y + Dy[dir];
					next.x = cur.x + Dx[dir]; //4 방향으로 이동
					next.time = cur.time + 1;

					if (next.y < 0 || next.y >= N || next.x < 0 || next.x >= N) continue; //판밖으로 나가면 다음 확인 

					//방문한적 없고 물고기의 크기가 상어의 크기보다 작으면 
					if (visited[next.y][next.x] == false && map[next.y][next.x] <= shark_size) {
						visited[next.y][next.x] = true;
						q.push(next);
					}
				}

			}

			if (is_map_update) { // 먹을 수 있는 물고기가 있으면
				shark = favorite;
				++shark_eat;
				if (shark_eat == shark_size) {
					++shark_size;
					shark_eat = 0;
				}
				map[shark.y][shark.x] = 0;  //물고기 먹고 맵 갱신

			}

		}

	answer = shark.time;
	return answer;
}
int main() {
	cin >> N;
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; j++) {
			cin >> map[i][j];
			if (map[i][j] == 9) {  //상어라면
				shark.x = j; shark.y = i;
				shark.time = 0;
				shark_size = 2; shark_eat = 0; // 초기 상어 값 세팅
				map[i][j] = 0;  // 상어가 나중에 이 위치로 이동 할 수 있도록 변경
			
			}
		}
	}

	cout << solve();
}