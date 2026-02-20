#include <iostream>
#include <string>
#include <algorithm>
#include <iostream>

using namespace std;

int main()
{
	string marks = "412";
	string str;
	int num;
	cin >> num;

	while (num > 0) {
		int temp = num % 3;
		str += marks[temp];
		if (temp == 0)

			num = num / 3 - 1;
		else num /= 3;
	}

	reverse(str.begin(), str.end());

	cout << str << endl;

	return 0;
}


