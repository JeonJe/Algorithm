//https://www.acmicpc.net/problem/1194

//빈 곳 : 언제나 이동할 수 있다. ('.‘로 표시됨)
//벽 : 절대 이동할 수 없다. (‘#’)
//열쇠 : 언제나 이동할 수 있다.이 곳에 처음 들어가면 열쇠를 집는다. (a - f)
//문 : 대응하는 열쇠가 있을 때만 이동할 수 있다. (A - F)
//민식이의 현재 위치 : 빈 곳이고, 민식이가 현재 서 있는 곳이다. (숫자 0)
//출구 : 달이 차오르기 때문에, 민식이가 가야하는 곳이다.이 곳에 오면 미로를 탈출한다. (숫자 1)
//달이 차오르는 기회를 놓치지 않기 위해서, 미로를 탈출하려고 한다.한 번의 움직임은 현재 위치에서 수평이나 수직으로 한 칸 이동하는 것이다.
//
//민식이가 미로를 탈출하는데 걸리는 이동 횟수의 최솟값을 구하는 프로그램을 작성하시오.\\입력
//첫째 줄에 미로의 세로 크기 N과 가로 크기 M이 주어진다.
//(1 ≤ N, M ≤ 50) 둘째 줄부터 N개의 줄에 미로의 모양이 주어진다. 
//같은 타입의 열쇠가 여러 개 있을 수 있고, 문도 마찬가지이다. 
//그리고, 영식이가 열쇠를 숨겨놓는 다면 문에 대응하는 열쇠가 없을 수도 있다.
//0은 한 개, 1은 적어도 한 개 있다. 그리고, 열쇠는 여러 번 사용할 수 있다.
//
//출력
//첫째 줄에 민식이가 미로를 탈출하는데 드는 이동 횟수의 최솟값을 출력한다. 만약 민식이가 미로를 탈출 할 수 없으면, -1을 출력한다.


#include <iostream>
#include <cstring>
#include <queue>

using namespace std;

const int MAX = 51;
char map[MAX][MAX];
bool visit[64][MAX][MAX]; // 열쇠가 6개이고 열쇠를 한번 이상 사용할 수 있다. => 비트마스킹
//6비트를 사용해서 LSB부터 a,b ... f까지 매칭 a,c 열쇠를 가지고 있으면 000101로 표현 => O(64*NM) => O(NM)

int N, M; // 세로 N, 가로 M

int Dx[] = { 0,0,-1,1 };
int Dy[] = { 1,-1,0,0 };

queue < pair<pair<int,int>, pair<int, int>>> q; //<y, x 좌표>,<탐색 횟수 ,열쇠>

int solve() {
	int min = 0;

	while (!q.empty()) {

		int qsize = q.size(); // 이번 횟수에 움직일 애들에 대해서

		for (int t = 0; t < qsize; t++) {  // 이번 횟수에 찾을 위치에 대하여 
			int y = q.front().first.first; // 현재 찾을 y,x 위치와 횟수, key 값
			int x = q.front().first.second;
			int cnt = q.front().second.first; // 현재까지 횟수
			int key = q.front().second.second; // 가지고 있는 key 

			q.pop();

			if (map[y][x] == '1') return cnt; // 현재의 위치가 1이라면 탈출

			for (int i = 0; i < 4; i++) { //4방향에 대해서 
				int ny = y + Dy[i];
				int nx = x + Dx[i];
				int nkey = key;
				
				if (ny < 0 || ny >= N || nx < 0 || nx >= M) continue; //  판 밖으로 나갈 시 확인 X
				
				if (map[ny][nx] == '#' || visit[key][ny][nx]) continue; // 벽이거나 방문한적 있으면 못지나감

				else if (islower(map[ny][nx])) // map이 열쇠일 때 					
					nkey |= 1 << (map[ny][nx] - 'a');  //  열쇠의 비트를 킨 것을 key에 더함. (or 연산으로)  => 키 습득
					//만약 D라면 001000 이고 이것을 key와 or 연산하여 key 에 3번째 자리가 1로 바뀜.
					// |=  : 연산자와 숫자를 사용하여 특정 비트를 킨다. or 연산
					
				else if (isupper(map[ny][nx])) // 문일 때 
					if (!(nkey & (1 << (map[ny][nx] - 'A')))) continue; 
				// 문의 알파벳을 비트로 표현하고 key 가 가지고 있는지 & 연산으로 확인
				// 키를 가지고 있지 않다면 continue
			
				//1) 열쇠가 있는 곳이거나, 2)문인데 해당 키가 있거나 3) 빈 곳이거나, 4) 민식이가 있던 곳이거나 5) 출구인 경우
				visit[nkey][ny][nx] = true; // 방문 표시
				q.push({ {ny,nx},{cnt + 1 , nkey} }); // 경로의수 + 1				
				
			}
		}		
	}

	return -1;

}
int main() {

	cin >> N >> M; // 세로 N, 가로 M
	memset(visit, false, sizeof(visit));

	for (int i = 0; i < N; ++i) {
		getchar();	//버퍼 비우기
		for (int j = 0; j < M; ++j) {
			map[i][j] = getchar(); // 한 글자씩 받기
			if (map[i][j] == '0') {
				q.push({ {i,j},{0,0} }); //탐색 횟수 0 , 키 0
				visit[0][i][j] = true; //i,j 위치 방문 표시 key는 가지지 않았으므로 0에 대입
			}
		}
	}

	cout << solve();

	return 0;
}
