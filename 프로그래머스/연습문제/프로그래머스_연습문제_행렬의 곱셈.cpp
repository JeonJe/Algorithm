//https://programmers.co.kr/learn/courses/30/lessons/12949
#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<vector<int>> solution(vector<vector<int>> arr1, vector<vector<int>> arr2) {
	vector<vector<int>> answer;
	int flag = 0;

	for (int i = 0; i < arr1.size(); i++) {  //arr1 의 row 수
		vector<int> temp;
		for (int j = 0; j < arr2[0].size(); j++) { //arr2의 col 수
			int sum = 0;
			for (int k = 0; k < arr1[0].size(); ++k) { //arr1의 col 수이자 arr2의 row 수
				sum += arr1[i][k] * arr2[k][j]; // k 가 공통적으로 들어감 
			}
			temp.push_back(sum);
		}
		answer.push_back(temp);

	}

	return answer;
}