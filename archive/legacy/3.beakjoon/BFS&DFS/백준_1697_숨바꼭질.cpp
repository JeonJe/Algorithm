#include <iostream>
#include <queue>
using namespace std;

int N, K; // N 은 술래, K 은 도둑

int visit[100001] = { 0, };

int solve() {

	queue<pair<int, int>> q;
	q.push(make_pair(N, 0));

	while (!q.empty()) {

		pair<int, int> curr = q.front();  // 꺼내고

		q.pop();

		if (curr.first < 0 || curr.first >100000 || visit[curr.first]) continue; // 범위 밖 또는 방문했던 곳은 continue

		if (curr.first == K) return curr.second; // 잡았으면 시간 리턴

		if (visit[curr.first] == 0) visit[curr.first] = 1; // 방문한적 없으면 방문표시

		q.push(make_pair(curr.first + 1, curr.second + 1));  // 다음 Breath 시간은 second 로 저장하고 + 1씩 추가
		q.push(make_pair(curr.first - 1, curr.second + 1));
		q.push(make_pair(curr.first * 2, curr.second + 1));

	}

}

int main() {

	cin >> N >> K;
	cout << solve();
	return 0;
}