#include <vector>
#include <iostream>
#include <unordered_map>
using namespace std;

vector<int> solution(vector<int> arr)
{
	vector<int> answer;
	int current = -1;
	for (int i = 0; i < arr.size(); i++) {
		if (current != arr[i]) {
			current = arr[i];
			answer.push_back(arr[i]);
		}
	}
	return answer;
}