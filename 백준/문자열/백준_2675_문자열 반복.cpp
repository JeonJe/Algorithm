#include <iostream>
#include <string>

using namespace std;


//문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.
//즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다.S에는 QR Code "alphanumeric" 문자만 들어있다.
//
//QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-. / : 이다.


int T;

int main() {
	string str;
	int rep;
	char ch[1000];
	cin >> T;

	for (int i = 0; i < T; ++i) {
		cin >>rep >> str;

		for (int i = 0; i < str.size(); i++) {
			char cur = str[i]; //한 문자에 대해 
			for (int j = i*rep; j < i*rep+rep; j++) {   //1~rep , rep + 1 ~ 2rep...
				ch[j] = cur;
				cout << ch[j];
			}

		}
		cout << endl;
	}
	return 0;
}