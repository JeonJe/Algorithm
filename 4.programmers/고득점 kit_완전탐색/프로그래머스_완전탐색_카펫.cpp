#include <string>
#include <vector>
#include <iostream>
#include <math.h>
using namespace std;

vector<int> solution(int brown, int red) {
	vector<int> answer;

	int row = 0, col = 0;
	int sum = brown + red;

	for (int i = 3; i <= (int)sqrt(sum); ++i) {  //col의 수

		if (sum % i == 0) { // sum 의 값이 col 의 수로 나누어 떨어진다면 -> red + brown = row * col 만족
			int col = i;
			int row = sum / i;
			if (red == (col - 2) * (row - 2)) {
				answer.push_back(row);
				answer.push_back(col);
			}

		}
	}

	return answer;
}