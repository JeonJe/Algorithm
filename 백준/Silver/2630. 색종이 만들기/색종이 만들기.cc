#include <iostream>
#include <vector>
using namespace std;

int const MAX = 128;
int N;
int arr[MAX][MAX];

int white = 0;
int blue = 0;

void dfs(int n, int start_x, int start_y) {
	int color = arr[start_y][start_x]; // 현재 위치의 색 

	for (int i = start_y; i < start_y + n; ++i) {
		for (int j = start_x; j < start_x + n; ++j) {
			if (arr[i][j] != color) {					//분할된 색종이 안의 색이 다르다면?
				dfs(n / 2, start_x + n/2, start_y);		// 제1사분면
				dfs(n / 2, start_x, start_y);			 //제2사분면
				dfs(n / 2, start_x, start_y + n/2);		 //제3사분면
				dfs(n / 2, start_x + n/2, start_y+n/2);	 //제4사분면
				return;

			}
		}
	}
	if (color == 1) blue++; // 현재색이 파란색이면 파란색 숫자 추가
	else white++;
	
}
int main() {

	cin >> N;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> arr[i][j];
		}
	}

	dfs(N,0, 0); // 0,0

	cout << white << endl << blue << endl;

	return 0;

}