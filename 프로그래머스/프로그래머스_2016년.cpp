#include <string>
#include <vector>

using namespace std;
int month[] = { 31,29,31,30,31,30,31,31,30,31,30,31 };	//2월은 윤년 = 29

string solution(int a, int b) {
	int sum = 0;
	string answer = "";

	for (int i = 0; i < a - 1; i++)
		sum += month[i];		

	sum += b;	//1월 1일 부터 입력한 날까지 총 일수 계산

	if (sum % 7 == 1)   answer = "FRI";
	else if (sum % 7 == 2)   answer = "SAT";
	else if (sum % 7 == 3)   answer = "SUN";
	else if (sum % 7 == 4)   answer = "MON";
	else if (sum % 7 == 5)   answer = "TUE";
	else if (sum % 7 == 6)   answer = "WED";
	else if (sum % 7 == 0)   answer = "THU";

	return answer;
}
