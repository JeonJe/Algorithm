//https://programmers.co.kr/learn/courses/30/lessons/42588

#include <string>
#include <vector>
#include <stack>

using namespace std;

vector<int> solution(vector<int> heights) {
	vector<int> answer;

	stack<pair<int, int>> st;
	st.push(make_pair(0, heights[0]));
	pair<int, int> current;

	for (int i = 0; i < heights.size(); i++) {

		if (st.top().second <= heights[i]) {
			while (!st.empty() && st.top().second <= heights[i])   // st 에서 계속 꺼내며 비교
				st.pop();

			if (st.empty())
				answer.push_back(0);
			else                                                // 앞에 자기보다 큰 건물에 신호가 부딪힘
				answer.push_back(st.top().first);
		}
		else
			answer.push_back(st.top().first);

		st.push(make_pair(i + 1, heights[i]));  //앞의 건물을 지우고 현재의 건물로 바꿈
	}

	return answer;
}