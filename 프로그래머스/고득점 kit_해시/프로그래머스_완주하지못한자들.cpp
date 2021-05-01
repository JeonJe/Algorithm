//https://programmers.co.kr/learn/courses/30/lessons/42576

#include <string>
#include <vector>
#include <algorithm>
using namespace std;

string solution(vector<string> participant, vector<string> completion) {
	string answer = "";
	sort(participant.begin(), participant.end()); // 참가자 오름차순 정렬
	sort(completion.begin(), completion.end()); // 완주자 오름차순 정렬

	for (int i = 0; i < completion.size(); i++) {  //완주자 명단 확인
		if (participant[i] != completion[i]) { // 참가자 명단이랑 완주자 명단이랑 다르다면
											//(오름차순정렬) 이고 크기가 1차이
			return participant[i];          //참가자에 있는 사람이 완주하지 못한 것
		}
	}

	return participant[participant.size() - 1];   // 정렬된 참가자 중 마지막 참가자가 완주하지 못함
}