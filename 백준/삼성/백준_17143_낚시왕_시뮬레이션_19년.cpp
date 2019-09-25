#include <iostream>
#include <cstring>   // memcpy , memset
using namespace std;

struct Shark {
	int s, d, z; //s = spped , d = direct , z = size
};

int Dc[] = {0,0,1,-1}; //위, 아래, 오른쪽, 왼쪽 순서로
int Dr[] = {-1,1,0,-0};		//세로 움직임

int R, C, M;  //R(row)  세로 크기, C(column) 가로 크기, M 상어 수
int r, c, s, d, z = 0;

Shark arr[100][100];


int solve() {
	int sum = 0;

	Shark backup[100][100];

	for (int t = 0; t < C; ++t) { // 낚시왕이 왼쪽에서 오른쪽으로

		for (int j = 0; j < R; ++j) { // 낚시왕으로 부터 가까운 곳부터
			if (arr[j][t].z > 0) {   //상어가 있다면? 
				sum += arr[j][t].z; // 낚시왕이 상어를 잡음
				arr[j][t].z = 0;
				break;              //1 마리 잡기 잡기 때문에 break
			}
		}

		memcpy(backup, arr, sizeof(arr)); // backup 배열에 현재 상어 위치 백업
		memset(arr, 0, sizeof(arr)); // 현재 판 0 으로 set 

		for (int i = 0; i < R; ++i) { // 격자판 row => 세로
			for (int j = 0; j < C; ++j) {
				Shark& curr = backup[i][j]; // 레퍼런스 변수, alias 로 사용
				if (curr.z > 0) {			// 상어가 있으면 이동
					int new_row = i + curr.s * Dr[curr.d]; //새로운 행 = 상어 속도 * 방향
					int new_col = j+ curr.s * Dc[curr.d]; //새로운 열 = 상어 속도 * 방향

					if (new_row < 0 ) { // 위로 이동하면서 격자판을 벗어나는 경우
						new_row = -new_row; // 아래 방향으로 방향을 바꾸어줌
						curr.d = 1;
					}
					if (new_row > R - 1) {  // 아래로 이동하면서 격자판을 벗어나는경우
						int q = new_row / (R - 1); // 몫이 짝수이면 아래 방향, 홀수이면 위방향
						int r = new_row % (R - 1); // row 의 어디 위치 인지
						if (q % 2 == 0) {         //아래 방향
							new_row = r;
						}
						else {
							new_row = (R - 1) - r; // row 의 어디 위치 인지
							curr.d = 0; // 위 방향
						} 
					}

					if (new_col < 0) {  // 왼쪽으로 이동하면서 격자판을 벗어나는 경우
						new_col = -new_col;
						curr.d = 2; // 오른쪽 방향으로 변경
					}
					if (new_col > C - 1) { //오른쪽으로 이동하면서 격자판 벗어나는 경우
						int q = new_col / (C - 1);
						int r = new_col % (C - 1);
						if (q % 2 == 0) {   //오른쪽 방향
							new_col = r;
						}
						else {   //왼쪽 방향인경우 
							new_col = (C - 1) - r;
							curr.d = 3;
						}
					}
					//위에까지 상어의 새로운 위치 계산

					if (arr[new_row][new_col].z < curr.z) {
						//최초에는 그냥 넣고, 이미 있다면? 더큰경우에만 입력
						arr[new_row][new_col] = curr; // 백업 배열에 저장해두었던 상어를 새로운 위치로
					}
				}
			}
		}
	}
	return sum;

}
int main() {
	cin >> R >> C >> M;
	for (int i = 0; i < M; i++) {
		cin >> r >> c >> s >> d >> z; // 초기 입력 
		arr[r - 1][c - 1] = { s, d - 1, z };
		// 0,0 부터 사용하기 위해 r-1, c-1  
		// direct도 0 부터사용하기 위해 -1
	}
	cout << solve() << endl;

	return 0;
}