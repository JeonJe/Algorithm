#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>
#include <cstring>

using namespace std;

char arr[1000000];
string str;
int cnt;

int main() {

	getline(cin, str);
	
	strcpy(arr, str.c_str()); // strtok 을 사용하기 위해 arr로 복사

	char* tok = strtok(arr, " "); // 공백으로 문자 분리 (앞문장은 tok으로)
	while (tok != NULL) {
		tok = strtok(NULL, " "); //공백으로 문자 분리 
		cnt++;
	}
	cout << cnt;
	return 0;
}