////https://programmers.co.kr/learn/courses/30/lessons/42746

#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

bool compare(string &a, string &b) {
	return a + b > b + a ? true : false;
}


string solution(vector<int> numbers) {
	string answer = "";
	vector<string> string_arr;
	for (int i = 0; i < numbers.size(); ++i) // 숫자를 스트링벡터로 변환
		string_arr.push_back(to_string(numbers[i]));

	sort(string_arr.begin(), string_arr.end(), compare);
	//벡터를 숫자의 자리수가 큰 순서부터 내림차순 정렬

	for (string i : string_arr) //숫자 자릿수가 큰수부터 문자열입력
		answer += i;


	if (answer[0] == '0') return "0"; //가장 큰 수가 0이면, "0"반환
	return answer;
}