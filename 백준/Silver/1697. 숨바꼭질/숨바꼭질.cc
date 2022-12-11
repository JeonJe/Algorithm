#include <iostream>
#include <queue>
using namespace std;

int N, K; // N 은 술래, K 은 도둑

int visit[100001] = { 0, };

int solve() {
	int time = 0;
	queue<pair<int, int>> q;

	q.push(make_pair(N, time));

	while (!q.empty()) {

		pair<int, int> curr = q.front();  // 꺼내고

		q.pop();

		if (curr.first < 0 || curr.first >100000 || visit[curr.first]) continue;

		if (curr.first == K) return curr.second; // 잡았으면 시간 리턴

		if (visit[curr.first] == 0) visit[curr.first] = 1;

		q.push(make_pair(curr.first + 1, curr.second + 1));
		q.push(make_pair(curr.first - 1, curr.second + 1));
		q.push(make_pair(curr.first * 2, curr.second + 1));

	}
	return time;
}

int main() {

	cin >> N >> K;
	cout << solve();
	return 0;
}