#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>
using namespace std;

int main() {


	string input;
	string temp = "";
	int result=0;
	bool minus = false;

	cin >> input;

	for (int i = 0; i <= input.size(); i++) {
		if (input[i] == '+' || input[i] == '-' || input[i] == NULL) {
			if (minus == true) result -= stoi(temp);
			else result += stoi(temp); //처음 - 를 만났거나, +를 만난경우 가지고 있던 값을 result 에 더함
			temp = "";
			if (input[i] == '-') minus = true; // 첫 '-' 뒤의 '+'들은 분배 법칙으로 -가 되고 다음 '-'을 만나면 괄호를 닫고 다시 열기 때문에 
												//계속 minus 만 함 => true 
			

		}
		else  // 숫자 일 경우 
			temp += input[i]; // 임시로 저장하는 temp 에 수를 입력
				
	}
	cout << result;



	return 0;
}