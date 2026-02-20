#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <algorithm>

using namespace std;

bool dfs(string from, vector<vector<string>>& tickets, vector<bool>& visited, vector<string>& temp, vector<string>& answer, int cnt)
{
	temp.push_back(from); // 항공기의 출발역들을 담는 배열

	if (cnt == tickets.size()) {
		answer = temp;
		return true;
	}

	for (int i = 0; i < tickets.size(); ++i) {
		if (tickets[i][0] == from && visited[i] == false) { // from이 티켓의 출발역이고 , 방문한적 없다면
			visited[i] = true; // 방문 표시, tickets 에서 배열을 삭제하는 것이 아니라 visited 라는 배열로 방문여부를 표시

			bool success = dfs(tickets[i][1], tickets, visited, temp, answer, cnt + 1); //해당 티켓의 도착지로 이어지는 경로탐색
			if (success) return true; // 경로가 완성되었다면 트루 ( dfs 끝 )
			visited[i] = false; // 아니라면 방문 표시를 다시 false로
		}
	}

	temp.pop_back(); // 다른 경우를 확인해보아야 하므로 삭제
	return false;

}


vector<string> solution(vector<vector<string>> tickets) {
	vector<string> answer, temp;   //dfs를 돌며 경로를 담는 배열 temp
	vector<bool> visited(tickets.size(), false);

	sort(tickets.begin(), tickets.end());
	dfs("ICN", tickets, visited, temp, answer, 0);
	return answer;
}