#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N;
vector<pair<int, int>> v;

int main() {
	cin >> N;
	int start, end = 0;
	for (int i = 0; i < N; i++) {
		cin >> start >> end;
		v.push_back(make_pair(end, start));
	}
	sort(v.begin(), v.end());

	//for (int i = 0; i < v.size(); i++) {
	//	cout << v[i].first << " " << v[i].second << endl;
	//}

	int prev_end = 0;
	int cnt = 0;

	for (int i = 0; i < v.size(); i++) {
		if (prev_end <= v[i].second) {	// 이전 회의 끝나는 시간보다 회의 시작 시간이 늦고
			prev_end = v[i].first;
			cnt++;
		}

	}
	cout << cnt;


}