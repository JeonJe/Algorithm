#include <string>
#include <vector>
#include <queue>
using namespace std;

int solution(vector<int> priorities, int location) {
	int answer = 0;
	queue<pair<int, int>> q;
	priority_queue<int>pq;

	for (int i = 0; i < priorities.size(); i++) {
		q.push(pair<int, int>(i, priorities[i]));
		pq.push(priorities[i]); //정렬하여 큐에 입력
	}

	while (!q.empty()) {
		pair<int, int> current = q.front(); // 대기목록의 가장 앞에 문서를 꺼내옴

		if (current.second == pq.top()) // 중요도가 제일 클 경우
		{
			if (current.first == location) { // 중요성 같은 것중 내가 알고 싶은 것
				return answer + 1;
			}
			else { // 중요성 같은 것 중 내가 알고 싶은 것이 아닐 경우       
				q.pop(); // 중요성 큰 것 부터 하나씩 지우기
				pq.pop();
				answer++; //위치 위치 이동
			}
		}
		else {   // 대기목록에서 중요도가 높은 문서가 한개라도 존재
			q.push(current); // 맨 뒤로 이동
 			q.pop(); // 맨 앞의 작업 삭제
		}

	}
	return answer;

}