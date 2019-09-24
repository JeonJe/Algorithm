#include <string>
#include <vector>
#include <map>

using namespace std;

int solution(vector<vector<string>> clothes) {
	int answer = 1;
	map<string, int> hash;

	for (int i = 0; i < clothes.size(); i++) {
		hash[clothes[i][1]]++;  // 해당 아이템 종류의 개수 증가
	}

	map<string, int>::iterator it; // map 에 접근 하기 위해 iterator

	for (it = hash.begin(); it != hash.end(); it++) {
		answer = answer * (it->second + 1);    // 아이템 종류 + 1 (선택하지 않은 경우 )
	}

	return answer - 1; // 모두 선택하지 않은 경우는 제외하므로 -1
}