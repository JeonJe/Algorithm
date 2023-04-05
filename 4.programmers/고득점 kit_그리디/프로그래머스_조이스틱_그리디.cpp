#include <iostream>
#include <string>
#include <vector>
#include <cstring>
#include <algorithm>
using namespace std;

// A부터 M 까지는 위로 방향 65 ~ 77 
//N 부터 Z 까지는 아래 방향으로 접근 78 ~ 90
int solution(string name) {
	int answer = 0;
	int size = name.size();
	int direction = name.size() - 1; // 최대 이동 횟수 

	for (int i = 0; i < size; i++) {
		int next = i + 1;
		char target_alp = name[i];

		if (target_alp <= 'N') answer += target_alp - 'A';
		else answer += 'Z' - target_alp + 1;

		while (next < size && name[next] == 'A') next++; 
		//오른쪽 방향으로 진행하면서 A를 만나면 건너 뜀

		direction = min(direction, i + size - next + min(i, size - next)); //모두 A가 될 때까지 오른쪽으로 이동하는 것과 왼쪽으로 이동하는 것중 작은것 
		// i + size - next : 왼쪽으로 돌아갔을 때 A가 아닌 것을 만날 때까지 이동한 횟수
		//min ( i , n-next ) : 현재 진행 인덱스와 뒤에서 가장 가까운 A가 아닌 인덱스 중 어떤 것이 더 적은지 비교
		//출처 https://jayrightthere.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A1%B0%EC%9D%B4%EC%8A%A4%ED%8B%B1
		

	}
	answer += direction;
	return answer;

	//또 다른 문제풀이로는 오른쪽 방향으로 "A"가 아닌 문자를 만나는 이동 횟수
	// 왼쪽 방향으로 "A"가 아닌 문자를 만나는 이동 횟수 
	// 비교해서 더 작은쪽으로 이동하고 "A" 문자와 target 문자의 차이를 asnwer 에 더하는 방법 
}


int main() {

	string str = "CANAANAA";
	cout << solution(str);
	return 0;

}