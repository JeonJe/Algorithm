//https://programmers.co.kr/learn/courses/30/lessons/12915#

#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

bool cmp(pair<char, string>&a, pair<char, string>&b) {
	return a < b; //n번째 인덱스 문자가 다를 경우 사전적으로 낮은게 먼저
				   //같을 경우 문자열 전체적으로 낮은게 먼저
}
vector<string> solution(vector<string> strings, int n) {
	vector<string> answer;
	vector <pair<char, string>> temp;

	for (auto i : strings)
		temp.push_back({ i[n],i });

	sort(temp.begin(), temp.end(), cmp);

	for (int i = 0; i < temp.size(); ++i)
		answer.push_back(temp[i].second);

	return answer;
}