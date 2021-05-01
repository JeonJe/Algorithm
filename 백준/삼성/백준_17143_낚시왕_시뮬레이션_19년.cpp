//https://www.acmicpc.net/problem/17143

#include <iostream>
#include <cstring>   // memcpy , memset
using namespace std;

struct Shark {
	int s, d, z; //s = spped , d = direct , z = size
};

int Dc[] = { 0,0,1,-1 }; // 상하좌우 이동
int Dr[] = { -1,1,0,0 };

int R, C, M;  //R(row) 배열의 y크기, C(column) 배열의 x크기, M  상어의수
int r, c, s, d, z = 0;

Shark arr[100][100];


int solve() {
	int sum = 0;

	Shark backup[100][100];

	for (int t = 0; t < C; ++t) { //  가로로 이동하면서 

		for (int j = 0; j < R; ++j) { // 격자판 세로
			if (arr[j][t].z > 0) {   // 상어의 크기가 0 일시 
				sum += arr[j][t].z; // 상어를 잡은것, 크기를 더해줌
				arr[j][t].z = 0;    // 그 위치의 상어는 없으므로 0
				break;              //수면으로부터 가까운 상어를 잡았으므로 break
			}
		}

		memcpy(backup, arr, sizeof(arr)); // backup에 arr 복사(상어 위치들)
		memset(arr, 0, sizeof(arr)); // 최종위치를 쓰기 위해 초기화

		for (int i = 0; i < R; ++i) { // 모든 위치의 상어를 확인하기 위해 이중 룹
			for (int j = 0; j < C; ++j) { // 가로 
				Shark& curr = backup[i][j]; // 간편하게 쓰기 위해 레퍼런스 변수, alias
				if (curr.z > 0) {		// 지금 상어 위치 
					int new_row = i + curr.s * Dr[curr.d]; //최종 위치 
					int new_col = j + curr.s * Dc[curr.d]; 
					//만약 방향이 위쪽이라면 Dr 은 0이고 0* 속도 이므로 좌,우 변화 X

					if (new_row < 0) { // 위로 격자판을 벗어났을 경우 
						new_row = -new_row; // 음수를 양수로 (아래로) 
						curr.d = 1;      //방향 
					}

					if (new_row > R - 1) {  // 아래 방향으로 벗어날 경우
						int q = new_row / (R - 1);  //방향 
						int r = new_row % (R - 1); // 위치
						if (q % 2 == 0) {         //몫이 짝수이면 아래 방향
							new_row = r;     //방향 그래도, 최종위치는 나머지
						}
						else {
							new_row = (R - 1) - r; //마지막 좌표에서 나머지 뺴기
							curr.d = 0; // 홀수일 경우 방향이 바뀌고
						}
					}

					if (new_col < 0) {  // 좌로 격자판을 벗어났을 경우 
						new_col = -new_col;
						curr.d = 2; // 오른쪽 방향으로 바꿔주기
					}
					if (new_col > C - 1) { // 오른쪽으로 마지막 열을 벗어났을 경우
						int q = new_col / (C - 1);
						int r = new_col % (C - 1);
						if (q % 2 == 0) {   //나머지가 최종 위치 
							new_col = r;
						}
						else {   // 마지막 열에 위치에서 나머지 뺌
							new_col = (C - 1) - r;
							curr.d = 3; // 왼쪽
						}
					}

					//새로운 위치의 상어의 크기보다 현재 상어의 크기가 크다면
					if (arr[new_row][new_col].z < curr.z) 
									arr[new_row][new_col] = curr;
					//새로운 위치에 이동
					
				}
			}
		}
	}
	return sum;  //잡은 상어 크기의 합 

}
int main() {
	cin >> R >> C >> M;
	for (int i = 0; i < M; i++) { //  상어의 수 만큼 반복문
		cin >> r >> c >> s >> d >> z; // 상어의 정보
		arr[r - 1][c - 1] = { s, d - 1, z };
		// 0,0 부터 시작하므로 r-1,c-1 에 상어의 정보 입력
		// direct은 0 부터 시작하므로 -1
	}
	cout << solve() << endl;

	return 0;
}