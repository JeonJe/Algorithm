#include <iostream>
#include <stack>

using namespace std;
stack <pair<int, int>> st;
int result[500001] = { 0, };
int N;

int main() {

	int height;

	cin >> N;
	cin >> height;

	st.push(make_pair(1, height));

	for (int i = 1; i < N; i++) {
		cin >> height;

		if (height > st.top().second) {
			while (!st.empty() && st.top().second < height) {
				st.pop();
			}

			if (st.empty()) result[i] = 0;
			else {
				result[i] = st.top().first;		//현재 탑의 신호가 부딪히는 탑
				if (st.top().second == height) st.pop(); // 앞에 탑은 현재 탑 때문에 더 이상 신호를 받지 못함
			}
		}
		else {
			result[i] = st.top().first;		//현재 탑의 신호는 최근 탑에 부딪힘.
		}


		st.push(make_pair(i + 1, height)); // 1부터 넣었으므로 2부터 넣기 위해 i+1
	}

	for (int i = 0; i < N; i++)
		cout << result[i] << " ";

	return 0;
}