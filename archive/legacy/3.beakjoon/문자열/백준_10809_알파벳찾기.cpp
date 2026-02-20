#include <iostream>
#include <string>
#include <cstring>

//알파벳 소문자로만 이루어진 단어 S가 주어진다.각각의 알파벳에 대해서,
//단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 - 1을 출력하는 프로그램을 작성하시오.

int alpha[26] = { -1, };

using namespace std;

int main() {
	memset(alpha, -1, sizeof(alpha));
	string str;

	cin >> str;

	char alp = 'a';
	int k = 0;

	while (k<26) {
	for (int i = 0; i < str.size(); i++) {
			if (alp == str[i]) { // 처음 나오는 같은 문자
				alpha[k] = i; // 문자의 위치 저장
				break;
			}
		}

		alp++; // 다음 문자 확인
		k++; // k 증가 
	}

	for (int i = 0; i < 26; i++) {
		cout << alpha[i] << " ";
	}

	
	return 0;
}