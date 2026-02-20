//https://programmers.co.kr/learn/courses/30/lessons/42577
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

bool solution(vector<string> phone_book) {

	bool answer = true;
	for (string s1 : phone_book) { // 배열 인덱싱 이터레이터 대신 사용 가능!
		for (string s2 : phone_book) {
			if (s1 != s2) { // 다른 문자
				if (s1.length() > s2.length()) { // s1 의 크기가 크면서
					if (s2 == s1.substr(0, s2.length())) //s1에서 0부터 s2 크기만큼 가져왔을 때 s2와 같다면
						return false;
				}
			}
		}
	}
	return answer;
}