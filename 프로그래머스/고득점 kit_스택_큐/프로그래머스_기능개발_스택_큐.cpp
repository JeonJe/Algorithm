//https://programmers.co.kr/learn/courses/30/lessons/42586

#include <string>
#include <vector>
#include <iostream>
#include <queue>
using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
	vector<int> answer;
	vector<int> q = progresses;
	vector<int> sq = speeds;

	while (!q.empty()) {
		int front = q[0];
		int qsize = q.size();

		if (front == 100) { // 먼저 배포되어야 하는 것이 개발이 다 되었으면
			int cnt = 0;
			while (true) {
				if (q.empty() || q[0] != 100)  { // 모두 배포되었거나 배포순서가 맞지 않으면
					answer.emplace_back(cnt); // 배포된 기능 수 추가 
					break;
				}
	
				q.erase(q.begin()); // 순차대로 배포중이면 큐에서 삭제
				sq.erase(sq.begin());
				cnt++; // 순차적으로 몇개가 배포되는지 체크
			}
		}
		else { // 먼저 배포되어야 하는 것이 개발이 되지 않았으면
			for (int i = 0; i < qsize; ++i) {
				q[i] += sq[i];
				if (q[i] > 100) q[i] = 100;
			}
		}
	}

	return answer;
}

int main()
{

	vector<int> prog ({ 93,30,55 });
	vector<int> speed({ 1,30,5 });

	vector<int> result = solution(prog, speed);
	for (int i = 0; i < result.size(); ++i) {
		cout << result[i] << " ";
	}
	return 0;
}