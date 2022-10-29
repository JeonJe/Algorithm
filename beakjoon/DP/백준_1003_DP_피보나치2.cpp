
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
		// N = 0:  ( 1,0 )
		// N = 1:  ( 0,1 )
		// N = 2:  ( 1,1 )
		// N = 3:  ( 1,1 ) + ( 0,1 )  = ( 1,2 )
		// N = 4:  ( 1,2 ) + ( 1,1 )  = ( 2,3 )
		// N = 5:  ( 2,3 ) + ( 1,2 )  = ( 3,5 )

		for (int i = 2; i <= n; i++)	//피보나치 반복문버전
		{
			list<tuple<int, int>>::iterator iter_1 = li.begin();
			list<tuple<int, int>>::iterator iter_2 = li.begin();

			advance(iter_1, i - 1); // N-1 번째 튜플 
			advance(iter_2, i - 2); // N-2 번째 튜플 
			li.push_back({ get<0>(*iter_1) + get<0>(*iter_2),get<1>(*iter_1) + get<1>(*iter_2) }); // 두 튜플의 값을 더해서 list 에 삽입
		}

		list<tuple<int, int>>::iterator output = li.begin();
		advance(output, li.size() - 1);

		cout << get<0>(*output) << " " << get<1>(*output) << endl; // N 번째 튜플 출력 
	}
}
