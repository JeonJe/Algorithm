#include <iostream>
#include <cstring>
#include <vector>

using namespace std;

int N, K;

bool backup[1001];
vector<pair<int, int>> v;

int del = 0;
int main() {

	int cnt = 0;
	cin >> N >> K; // K 번째 지우눈 수

	memset(backup, false, sizeof(backup));

	for (int i = 2; i < N + 1; ++i) {

		for (int j = i; j <= N; j += i) { // 현재 i 의 배수들을 backup array에서 true체크
			if (backup[j] == false) { // 배수로 입력이 안된 수면
				backup[j] = true; //true
				cnt++;			//몇 번째로 체크되었는지 확인
				v.push_back(make_pair(j, cnt)); // 현재 값와 몇 번째 수인지 벡터에 담기
			}
		}
	}

	cout << v[K - 1].first << endl;

	return 0;
}