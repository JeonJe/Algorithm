//https://programmers.co.kr/learn/courses/30/lessons/12973
#include <iostream>
#include <string>
#include <stack>

using namespace std;

int solution(string s)
{
	int answer = 0;
	stack<char> st;

	for (int i = 0; i < s.size(); ++i) {
		if (st.empty() || st.top() != s[i]) { //스택이 비어있거나, 탑과 현재 문자가 다르다면
			st.push(s[i]); //현재문자를 스택으로 
		}
		else { //두 문자가 짝
			st.pop();
		}
	}

	if (st.empty()) answer = 1;

	return answer;
}