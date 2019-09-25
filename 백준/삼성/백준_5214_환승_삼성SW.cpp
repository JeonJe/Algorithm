#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int N, K, M;
//역의 수 N, 하이퍼 튜브가 서로 연결하는 역의 개수 K
//하이퍼튜브의 개수 M

//최악의 경우 1000개의 하이퍼튜브가 서로 연결하는 역의 개수가 1000개이면
//1000^3 이므로 메모리초과 
//int arr[1001][1001]; => 메모리초과남

vector<int> v[1000000+ 2000]; // 2000  은 하이퍼튜브를 가상의 역
int visit[1000000 + 2000]; // 해당 인덱스에 도달하는데 지나친 역의 수
s
// 1 : 10 11   => 1이 들어있는 곳은 10번과 11번
// 2 : 10	   => 2이 들어있는 곳은 10번
// 3 : 10 12
// 4 : 11
// 5 : 11 13
// 6 : 12 13 14
// 7 : 12 13
// 8 : 14
// 9 : 14

// 10 : 1 2 3 => 입력으로 들어온 하이퍼 튜브 
// 11 : 1 4 5
// 12 : 3 6 7
// 13 : 5 6 7
// 14 : 6 8 9

int solve() {

	visit[1] = 1; // 출발역
	queue<int> q;
	q.push(1);   
	
	while (!q.empty()) {
		int curr = q.front();
		q.pop();
		 
		for (auto i : v[curr]) { // 출발역이 같은 역 확인 

			if (!visit[i]) {   // ex) curr이 1이면 v[1] 에는 10,11에 대해 확인, 첫 방문시에대해
				visit[i] = visit[curr] + 1; // 첫 방문시 1증가
				q.push(i);		//다음에 확인 할 역에 추가 
			}

		}
	
	
	}
	int result = 0;
	visit[N] ? (result = visit[N] / 2 + 1) : (result = -1);
	//N으로 들어온 수에 대해 도착 할 수 없다면 -1
	// 도착 할 수 있다면 visit[N] -> 첫 방문과 그 다음 확인할 역에 대해 세어줘서 * 2배가 되었음
	// => / 2 를 해준 뒤 + 1 

	return result;

}
int main() {

	int num; 
	cin >> N >> K >> M;  // 0부터 N 까지는 실제역 저장, N+1 부터는 하이퍼튜브역
	for (int i = N + 1; i <= N + M; ++i) {
		for (int j = 0; j < K; ++j) { 
			cin >> num;
			v[i].push_back(num); //v에 하이퍼 튜브역 저장
			v[num].push_back(i); //정점을 역으로
		}
	}

	cout << solve();

	return 0;
}