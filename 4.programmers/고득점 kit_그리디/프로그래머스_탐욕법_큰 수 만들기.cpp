#include <iostream>
#include <string>
#include <vector>

using namespace std;

string solution(string number, int k) {
	string answer = "";
	int start = -1;
	int answer_size = number.size() - k; //return 되는 숫자의 크기
	int new_j = 0;

	for (int i = 0; i < answer_size; i++) { //  k개를 제외한 수의 최대값
		int max = -1;
		for (int j = start + 1; j < number.size() - (answer_size - i) + 1; j++) {  //range 는 start+1 ~ 뒤에서부터 i개 제외 
																		 //range 는 점점 뒤로 이동
			if (max < number[j] - '0') {//제외 한 수 중 가장 큰 수 찾기 , atoi 기능
				max = number[j] - '0';
				new_j = j; // 최대값의 인덱스 저장
			}
		}

		answer.append(to_string(max)); // 최대값을 가진 수를 이어 붙이기 
		start = new_j; // 뒤에서 i 개를 제외한 수 중 가장 큰 수부터 그 뒤에 값중 찾기
	}
	return answer;
}
int main() {
	string number = "4177252841";
	int k = 4;
	cout << solution(number, k);
}
