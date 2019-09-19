#include <string>
#include <vector>
#include <queue>
#include <list>
#include <algorithm>

using namespace std;

int solution(int n, vector<vector<int>> edge) {
	int answer = 0;
	vector<list<int>> graph(n + 1, list<int>()); //graph 그리기 위해 사용
	vector<int> dist(n + 1, 0); //1에서 부터 해당 노드까지 거리를 담기 위해 사용 
								//크기 n+1, 0 으로 초기화
	vector<bool> visit(n + 1, false);  // 노드 방문 여부 체크 
	queue<int> q;	//노드 번호 입력 

	for (auto it = edge.begin(); it != edge.end(); it++) {
		graph[(*it).front()].push_back((*it).back());   //at() , [] 가 없음 
		graph[(*it).back()].push_back((*it).front());
	}

	q.push(1);
	visit[1] = true;	//노드 1부터 확인 
	dist[1] = 0;

	while (!q.empty()) {
		int current = q.front();   // 현재 확인하려는 노드 번호
		q.pop();

		for (auto i : graph[current]) {
			if (visit[i] == false) {   // 그래프에서 연결된 노드 i 확인
				visit[i] = true; //방문한적이 없으면 방문으로 바꾸고
				q.push(i);		// 노드 방문 하기 위해 queue에 삽입
				dist[i] = dist[current] + 1;	//current 노드에서 +1 거리 증가
			}
		}
	}

	int max = *max_element(dist.begin(), dist.end()); // 가장 멀리 있는 노드 값

	for (auto i : dist) {	// 가장 멀리 있는 노드의 수 확인
		if (i == max) answer++;
	}

	return answer;
}