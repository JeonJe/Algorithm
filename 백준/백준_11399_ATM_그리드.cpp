#include <iostream>
#include <algorithm>
#include <vector>
#include <numeric>
using namespace std;

int N;
int arr[1001] = { 0, };
vector<int> sum;

int main() {
	cin >> N;
	for (int i = 0; i < N; i++)
		cin >> arr[i];

	sort(arr, arr + N); // 돈을 뽑는데 걸리는 시간을 오름차순 정렬

	sum.push_back( arr[0] ); // 가장 빨리 돈을 뽑을 수 있는 사람의 소요 시간
	for (int i =1; i < N; i++) 
		sum.push_back( sum[i - 1] + arr[i]); // 이전 대기 시간 + 자기의 ATM 소요 시간
	 
	cout << accumulate(sum.begin(), sum.end(), 0); // 합계 
	
	return 0;
}