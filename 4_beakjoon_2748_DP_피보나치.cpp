#include <iostream>
#include <cstring>
using namespace std;

int n;
long long arr[100];		
//int 로 작성할 시 n 이 큰수일 경우 음수로 표현, long, double 이 아닌 long long

int main()
{
	memset(arr, 0, sizeof(arr));
	cin >> n;

	arr[0] = 0;
	arr[1] = 1;

	for (int i = 2; i <= n; i++)	//피보나치 반복문버전
		arr[i] = arr[i - 1] + arr[i - 2 ];

	cout << arr[n] << endl;
}