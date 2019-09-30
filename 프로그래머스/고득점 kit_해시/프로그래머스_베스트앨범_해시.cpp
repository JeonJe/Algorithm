#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>

using namespace std;

				//장르 , 재생 횟수, 인덱스 
bool compare(tuple<string, int, int>& a, tuple<string, int, int>& b) {
	if (get<1>(a) == get<1>(b))			 // 장르 내에서 재생횟수가 같은 노래 중에서 
		return get<2>(a) < get<2>(b);	//고유 번호가 낮은 노래를 먼저 수록
	return get<1>(a) > get<1>(b);		 // 장르 내에서 많이 재생된 노래를 먼저 수록
}

vector<int> solution(vector<string> genres, vector<int> plays) {

	vector<int> answer;
	map<string, int>hash;
	map<int, string, greater<int>> check;

	for (int i = 0; i < genres.size(); ++i) {
	
		if (hash.find(genres[i]) == hash.end()) hash[genres[i]] = plays[i];
		else hash[genres[i]] += plays[i]; // hash에 존재하는 장르라면 재생 횟수만 추가
	}
	for (auto it = hash.begin(); it != hash.end(); it++) {
		check[it->second] = it->first;
		//check[재생횟수] = 장르
	}

	vector<tuple<string, int, int>> songs; // 장르, 재생횟수, 인덱스

	for (int i = 0; i < genres.size(); i++) {
		songs.emplace_back(make_tuple(genres[i], plays[i], i)); // push_back 보다 빠른 emplace_back
	}

	sort(songs.begin(), songs.end(), compare); // 노래의 재생 횟수, 고유 번호로 정렬

	for (auto it = check.begin(); it != check.end(); it++) { // 재생횟수이 인덱스인 check 배열
		int temp = 0;
		for (int j = 0; j < songs.size(); j++) {
			if (get<0>(songs[j]) == it->second) { // 현재 노래가  check 에 담긴 장르라면
				answer.emplace_back(get<2>(songs[j])); // 현재의 인덱스를 넣음 , 내림차순이기 때문에 높은 수 부터
				temp++;
			}
			if (temp == 2) break;	//많이 재생된 노래를 2개 모았으면 탈출
		}
	}

	return answer;
}

int main() {
	vector<string> genres ;
	genres.push_back("classic");
	genres.push_back("pop");
	genres.push_back("classic");
	genres.push_back("classic");
	genres.push_back("pop");

	vector<int> plays;
	plays.push_back(500);
	plays.push_back(600);
	plays.push_back(150);
	plays.push_back(800);
	plays.push_back(2500);

	vector<int> answer = solution(genres, plays);

	for (int i = 0; i < answer.size(); i++) {
		cout << answer[i] << " ";
	}
	return 0;
}