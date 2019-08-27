
#include <iostream>
#include <cstring>
#include <tuple>
#include <list>

using namespace std;
int T;
int n;

int main()
{
	list <tuple<int, int>> li;
	cin >> T;

	for (int j = 0; j < T;j++) {

		li.clear();
		cin >> n;

		if (n == 0)		li.push_back({ 1,0 });
		else if (n == 1)		li.push_back({ 0,1 });
		else {
			li.push_back({ 1,0 });
			li.push_back({ 0,1 });
		}
		
		for (int i = 2; i <= n; i++)	//피보나치 반복문버전
		{asdfsadf
			list<tuple<int, int>>::iterator iter_1 = li.begin();
			list<tuple<int, int>>::iterator iter_2 = li.begin();

			advance(iter_1, i - 1);
			advance(iter_2, i - 2);
			li.push_back({ get<0>(*iter_1) + get<0>(*iter_2),get<1>(*iter_1) + get<1>(*iter_2) });
		}

		list<tuple<int, int>>::iterator output = li.begin();
		advance(output, li.size() - 1);

		cout << get<0>(*output) << " " << get<1>(*output) << endl;
	}
}
