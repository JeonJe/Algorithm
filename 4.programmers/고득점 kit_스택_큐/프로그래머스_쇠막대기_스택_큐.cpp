//https://programmers.co.kr/learn/courses/30/lessons/42585
#include <iostream>
#include <string>
#include <vector>
#include <stack>
using namespace std;


int solution(string arrangement) {

	stack<char> s;
	int answer = 0;

	for (int i = 0; i < (int)arrangement.size(); ++i) {
		if (arrangement[i] == '(')  //쇠파이프 수 증가 
			s.push('(');

		else {
			s.pop();
			if (arrangement[i - 1] == ')')
				answer += 1;

			// ')' 이전 문자가 ')' 이면 이전 문자가 쇠파이프 끝 부분 추가 +1

			else if (arrangement[i - 1] == '(')
				answer += (int)s.size();

			// ')' 이전 문자가 ')' 만날 시 이전 문자가  '(' 이면 -> 레이저 stack 사이즈만큼 +
			// 레이저로 쇠파이프 개수만큼 분리 

		}
	}
	return answer;
}

int main()
{
	string str = "(((()(()()))(())()))(()())";
	cout << solution(str);
	return 0;
}