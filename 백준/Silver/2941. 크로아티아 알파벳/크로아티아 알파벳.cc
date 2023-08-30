#include <iostream>
#include <string>

using namespace std;
string str;

int solution(string str) {
	int cnt = 0;
	int size = str.length();
	for (int i = 0; i < size; ++i) {
 
		if (str[i] == 'd' && i + 1 < size) {
			if (str[i + 1] == '-') i++;
			else  if (i + 2 < str.length()) {
				if (str[i + 1] == 'z' && str[i + 2] == '=') i+=2;
			}
		}
		else if (str[i] == 'c' && i + 1 < size) {
			if (str[i + 1] == '=' || str[i + 1] == '-') i++;
		}
		

		else if (str[i] == 'l' && i + 1 < size) {
			if (str[i + 1] == 'j') i++;
		}
				

		else if (str[i] == 'n' && i + 1 < size) {
			if (str[i + 1] == 'j') i++;
		}
					

		else if (str[i] == 's' && i + 1 < size) {
			if (str[i + 1] == '=') i++;
		}
						

		else if (str[i] == 'z' && i + 1 < size) {
			if (str[i + 1] == '=') i++;
		}
		cnt++;

	}

	return cnt;

}
int main()
{
	cin >> str;
	cout << solution(str);
	return 0;
}