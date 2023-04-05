#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

bool check(const string& tree, const string& skill) {
	bool broken = false;
	int prev = 0;
	for (auto s : skill) {  //각 스킬에 대해서
		int cur_index = tree.find(s); //유저의 스킬트리에서 스킬위치 찾기
		if (cur_index != -1) { //스킬트리에 스킬이 존재하지 않으면
			if (broken || cur_index < prev) return false;
			//현재 스킬트리가 이전에 배운 스킬보다 먼저배워야하는 스킬이라면
			//false
			else prev = cur_index;
		}
		else {
			broken = true; //첫 번째 스킬이 존재하지 않으면,
						//다음 스킬은 스킬트리를 위반하므로 return false

		}
	}
	return true;

}


int solution(string skill, vector<string> skill_trees) {
	int answer = 0;

	for (auto tree : skill_trees) { // 유저들의 스킬트리 확인
		if (check(tree, skill)) ++answer; // 유저의 스킬트리의 순서가 정확하다면 증가
	}
	return answer;
}

