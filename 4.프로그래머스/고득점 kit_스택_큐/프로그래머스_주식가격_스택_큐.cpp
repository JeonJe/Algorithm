//https://programmers.co.kr/learn/courses/30/lessons/42584
#include <string>
#include <vector>
#include <iostream>
#include <stack>

using namespace std;

vector<int> solution(vector<int> prices) {
	vector<int> answer(prices.size());
	
	for (int i = 0; i < prices.size(); ++i) { //현재 주식 가격
		int cnt = 0;
		for (int j = i+1; j < prices.size(); ++j) { //현재 다음의 주식 가격들
			if (prices[i] <= prices[j]) {
				answer[i]++; //가격이 하락하지 않은 경우
			}
			else { //가격이 하락할 경우 
				answer[i]++;
				break;
			}
		}
	}
	
	return answer;
}

int main()
{
	vector<int> p({ 1,2,3,2,3 });
	vector<int> result = solution(p);

	for (int i = 0; i < result.size(); i++)
		cout << result[i] << " ";

	return 0;
}