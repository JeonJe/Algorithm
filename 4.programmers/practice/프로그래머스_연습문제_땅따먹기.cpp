//https://programmers.co.kr/learn/courses/30/lessons/12913
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int DP[100000][4] = { 0, };
int solution(vector<vector<int>> land)
{
	int answer = 0;
	int n = land.size() - 1; // 3줄일경우 2

	for (int i = 0; i < 4; ++i) // 처음 행에서 선택 
		DP[0][i] = land[0][i];

	for (int i = 1; i < n + 1; ++i) { // 그 다음 row 에 대해 DP
		DP[i][0] = max(DP[i - 1][1], max(DP[i - 1][2], DP[i - 1][3])) + land[i][0];
		DP[i][1] = max(DP[i - 1][0], max(DP[i - 1][2], DP[i - 1][3])) + land[i][1];
		DP[i][2] = max(DP[i - 1][0], max(DP[i - 1][1], DP[i - 1][3])) + land[i][2];
		DP[i][3] = max(DP[i - 1][0], max(DP[i - 1][1], DP[i - 1][2])) + land[i][3];
	}
	return max(DP[n][0], max(DP[n][1], max(DP[n][2], DP[n][3])));
}