#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;


//<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
//철수는 이 지도를 가지고 연결된 집들의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
//여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다.
//대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다
//.지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

int N;
int arr[26][26];
bool visit[26][26];  //집 방문 여부 확인

int x_point[4] = { 1,0,-1,0 };   // 4 방향으로 인접한 집이 존재하는지 확인
int y_point[4] = { 0,-1,0,1 };

int cnt = 0; //단지 수 
int num_resident[1000] = { 0, }; // 단지의 집의 개수 

int DFS(int y, int x) {

	visit[y][x] = true; // 방문 체크
	num_resident[cnt]++; // 단지의 집의 수 증가

	for (int z = 0; z < 4; z++) {
		int new_x = x + x_point[z];
		int new_y = y + y_point[z];

		if (0 <= new_x && new_x < N && 0 <= new_y && new_y < N) {
			if (visit[new_y][new_x] == false && arr[new_y][new_x]) DFS(new_y, new_x);
			// 인접한 방문하지 않은 집 존재하면 DFS
		}
	}
	return 0;
}
int main()
{
	cin >> N;
	for (int i = 0; i < 26; i++) {
		memset(arr[i], 0, sizeof(int) * 26);
		memset(visit[i], false, sizeof(bool) * 26);	//초기화
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			scanf("%1d", &arr[i][j]);	//지도 입력
		}
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (arr[i][j] && visit[i][j] == false) { // 왼쪽 위 부터 순차적으로 조사
				DFS(i, j);
				cnt++; //단지 증가
			}
		}
	}

	cout << cnt << endl;
	sort(num_resident, num_resident + cnt); // 오름차순 

	for (int i = 0; i < cnt; i++) {
		cout << num_resident[i] << endl;
	}

	return 0;
}