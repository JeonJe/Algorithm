#include<string>
#include <iostream>
#include <stack>

using namespace std;

bool solution(string s)
{
	bool answer = true;
	stack <char> st;
	for (int i = 0; i < s.size(); i++) {
		char cur = s[i]; // 현재 문자
		if (cur == '(') { // ( '(' 라는 문자일 경우 
			st.push(cur);
		}
		else { // ( ')' 라는 문자일 경우 
			while (!st.empty() && st.top() != '(') { // 스택이 비어있지 않았고, '(' 가 아니라면
				st.pop(); //'(' 가 나올때까지 pop
			}
			if (st.empty()) return false; //짝이 없으면 거짓 리턴
			st.pop(); // 짝이 있으면  그 '(' 는 사용했기 때문에 pop
		}
	}
	if (!st.empty()) return false;

	return answer;
}