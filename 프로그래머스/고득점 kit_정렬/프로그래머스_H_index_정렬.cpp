#include <string>
#include <vector>
#include <functional>
#include <algorithm>

using namespace std;

int solution(vector<int> citations) {
	int answer = 0; // 6 5 3 1 0 6 을 가져와서 6번이상 인용된논문 6개 찾기
				 //나머지 논문이 6번 이하인용된거 찾기


	sort(citations.begin(), citations.end(), greater<int>());
	int  j = 0;
	for (int i = 0; i < citations.size(); i++) { //n편의 논문 중
		int h = citations[i]; // h번 

		if (citations[j] <= j) break; // h번 이상 인용된 논문이라면 
		j++;

	}
	return j;
}