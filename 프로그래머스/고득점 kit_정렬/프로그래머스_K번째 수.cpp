

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
	vector<int> answer;
	vector<int> new_array;

	for (int i = 0; i < commands.size(); i++) {
		new_array.clear();
		for (int j = commands[i][0]; j <= commands[i][1]; j++) {   // 2���� ���ʹ� 2�����迭�� ����
			new_array.push_back(array[j - 1]);  // �迭�� 0�� ���� �ε���
		}
		sort(new_array.begin(), new_array.end());
		answer.push_back(new_array[commands[i][2] - 1]); 
	}

	return answer;
}