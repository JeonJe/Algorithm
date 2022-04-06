#include <iostream>
#include <cstring>

using namespace std;

int N;
int visit[200];

int solve(string str) {

	int check = 0;
	for (int i = 0; i < str.length(); ++i) {
		if (visit[int(str[i])] == 0) { // 처음 나왔다면
			int temp = int(str[i]);  //처음 나온 알파벳을 담고
			while (1) {

				if (temp != str[i]) { //연속적으로 나오지 않을 때까지
					--i;    //연속적으로 나오지 않은 곳부터 다시 체크하기 위해 감소
					break;
				}
				visit[int(str[i])]++; // 값 증가 
				i++;

			}
		}
		else  // 그룹 단어가 아니라면
			return 0;
	}
	return 1;
}
int main() {
	int result = 0;
	cin >> N;
	string str;

	for (int i = 0; i < N; i++) {
		memset(visit, 0, sizeof(visit));
		cin >> str;
		result += solve(str);
	}

	cout << result;
	return 0;
}