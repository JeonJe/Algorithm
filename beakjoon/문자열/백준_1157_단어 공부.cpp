#include <iostream>
#include <string>
#include <cstring>

using namespace std;

//알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
//단, 대문자와 소문자를 구분하지 않는다.

int arr[26];
int main()
{
	string str;
	char cur;
	int max = -1;
	int index = -1;
	bool flag = false;

	memset(arr, 0, sizeof(arr));

	cin >> str;

	for (int i = 0; i < str.size(); ++i) {
		if (islower(str[i]))       //소문자이면?
			cur = toupper(str[i]); //대문자로 변환
		else 
			cur = str[i];
		
		int num(cur); // 아스키 숫자로 변환
		arr[cur - 65]++;

	}

	for (int i = 0; i < 26; i++) { //알파벳 a 부터 z 까지
		if (max < arr[i]) {  
			max = arr[i]; // 최대 빈도수를 가진 알파벳 이라면
			index = i + 65; // 현재 알파벳 + 65 로 대문자 아스키 코드 저장
			flag = false; // 여러개 존재 x
		}
		else if (max == arr[i]) { //가장 많이 사용된 알파벳이 여러개 존재하면  flag를 true
			flag = true;
		}
	}
	
	
	if (flag) cout << "?";
	else {
		char result(index); // 아스키 코드로 대문자 생성
		cout << result;
	}

}
