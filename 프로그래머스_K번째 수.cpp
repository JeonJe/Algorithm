#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
	vector<int> answer;
	vector<int> new_array;

	for (int i = 0; i < commands.size(); i++) {
		new_array.clear();
		for (int j = commands[i][0]; j <= commands[i][1]; j++) {   // 2차원 벡터는 2차원배열로 생각
			new_array.push_back(array[j - 1]);  // 배열은 0번 부터 인덱싱
		}
		sort(new_array.begin(), new_array.end());
		answer.push_back(new_array[commands[i][2] - 1]); 
	}

	return answer;
}