#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <numeric>


using namespace std;
bool arr[10000000] = { false, };


bool checkPaper(int i, string numbers) {
	bool flag = false;
	vector<bool> visit(numbers.size()); //숫자만큼 visit 배열 생성

	while (i != 0) { //소수로 판별된 수를 digit으로 분해 
		flag = false;
		int digit = i % 10;

		for (int j = 0; j <= numbers.size(); ++j) {
			if (digit == numbers[j] - '0' && visit[j] == false) {
				flag = true;  //digit 이 종이에 적힌 숫자이면 플래그 확인
				visit[j] = true;
				break;
			}
		}

		if (flag == false) return false; //종이 어느곳에도 적히지 않은 숫자이므로 false 리턴
		i = i / 10;       // 소수의 digit 모두가 종이에 적혀있는지 확인하기 위해 다시 digit 을 쪼갬   
	}
	return true;
}

int solution(string numbers) {
	int answer = 0;
	vector<int> prime;

	sort(numbers.begin(), numbers.end(), greater<char>());
	int range_max = stoi(numbers);

	for (int i = 2; i <= range_max; i++) {
		if (arr[i] == false && checkPaper(i, numbers)) { //소수이면서 종이에 적힌 숫자를 사용
			cout << i << endl;
			answer++;
		}
		if (arr[i] == false) { //소수
			for (int j = i; j <= range_max; j += i) { //소수의 배수는 소수가 아님
				arr[j] = true;
			}
		}
	}
	return answer;
}