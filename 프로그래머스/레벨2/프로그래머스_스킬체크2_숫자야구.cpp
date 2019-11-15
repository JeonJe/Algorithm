#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<vector<int>> baseball) {
	int answer = 0;

	for (int i = 123; i <= 987; i++) {
		int a = i / 100; // 백의 자리 
		int b = (i / 10) % 10; // 십의 자리
		int c = (i % 10); //일의 자리

		if (a == 0 || b == 0 || c == 0) continue; // 숫자가 0인 경우 제외
		if ((a == b) || (b == c) || (c == a)) continue; //같은 경우 제외 

		for (int j = 0; j < baseball.size(); j++) {
			int strike = 0; int ball = 0;

			int expt_num = baseball[j][0]; //현재 예측 숫자
			int expt_a = expt_num / 100; // 예상 하는 숫자의 백의 자리
			int expt_b = (expt_num / 10) % 10; // 예상 하는 숫자의 십의 자리
			int expt_c = (expt_num % 10); // 예상 하는 숫자의 일의 자리 

			if (a == expt_a) strike++; // 자릿수가 맞으면 strike
			if (b == expt_b) strike++;
			if (c == expt_c) strike++;

			if (strike != baseball[j][1]) break; // 스트라이크의 갯수가 다르면 해당 경우 확인 X

			if (a == expt_b || a == expt_c) ball++;
			if (b == expt_c || b == expt_a) ball++;
			if (c == expt_a || c == expt_b) ball++;
			if (ball != baseball[j][2]) break; //볼의 갯수가 다르면 해당 경우 확인 X

			if (j == baseball.size() - 1) answer++;

		}
	}

	return answer;
}