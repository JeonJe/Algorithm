#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <algorithm>
using namespace std;

int arr[1000];
int result[1000];
int T;

int main()
{
	int a, b;
	int max, maxIndex=0;

	cin >> T;
	for (int i = 0; i < T; ++i) {
		memset(arr, 0, sizeof(arr));

		cin >> a;
		for (int j = 0; j < 1000; ++j){
			cin >> b;
			arr[b]++;  //빈도수 증가
		}

		max = 0;
		maxIndex = 0;
		for (int k = 0; k < 1000; ++k) {
			if (arr[k] >= max) {  // 최빈도수 가진 숫자 찾기. 빈도가 같을땐 
								// 큰 숫자를 출력하기 위해 0부터 1000 순으로
				max = arr[k];   // 최빈도 수 arr[k]
				maxIndex = k;   // 그 인덱스
			}
		}

		cout << "#" << a << " " << maxIndex;
		if (i != 9) cout << endl;

	}
}